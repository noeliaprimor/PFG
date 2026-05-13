#!/usr/bin/env python3
import argparse

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    avg,
    col,
    count,
    current_timestamp,
    expr,
    from_json,
    lit,
    max as spark_max,
    min as spark_min,
    sum as spark_sum,
    to_json,
    to_timestamp,
    unix_timestamp,
    when,
    window,
    struct,
)
from pyspark.sql.types import DoubleType, StringType, StructField, StructType


def build_spark() -> SparkSession:
    spark = (
        SparkSession.builder
        .appName("M3T3AdvancedKafkaSparkStreaming")
        .master("local[*]")
        .config("spark.sql.shuffle.partitions", "4")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")
    return spark


def process_batch(batch_df, batch_id: int, output_base: str, bootstrap_server: str, enriched_topic: str) -> None:
    if batch_df.rdd.isEmpty():
        print(f"Batch {batch_id}: sin datos")
        return

    valid = (
        batch_df
        .filter(col("event_id").isNotNull())
        .filter(col("event_ts").isNotNull())
        .filter(col("customer_id").isNotNull())
        .filter(col("merchant_id").isNotNull())
        .filter(col("amount").isNotNull())
        .filter(col("amount") > 0)
        .dropDuplicates(["event_id"])
        .withColumn("amount_bucket", when(col("amount") >= 800, lit("high")).otherwise(lit("normal")))
        .withColumn("latency_seconds", unix_timestamp("processed_time") - unix_timestamp("event_ts"))
        .withColumn("batch_id", lit(batch_id))
    )

    invalid = (
        batch_df
        .filter(
            col("event_id").isNull()
            | col("event_ts").isNull()
            | col("customer_id").isNull()
            | col("merchant_id").isNull()
            | col("amount").isNull()
            | (col("amount") <= 0)
        )
        .withColumn(
            "error_reason",
            when(col("event_id").isNull(), lit("missing_or_malformed_event_id"))
            .when(col("event_ts").isNull(), lit("missing_or_malformed_event_time"))
            .when(col("customer_id").isNull(), lit("missing_customer_id"))
            .when(col("merchant_id").isNull(), lit("missing_merchant_id"))
            .when(col("amount").isNull(), lit("missing_amount"))
            .otherwise(lit("invalid_amount"))
        )
        .withColumn("batch_id", lit(batch_id))
        .select("raw_value", "error_reason", "topic", "partition", "offset", "processed_time", "batch_id")
    )

    merchant_metrics = (
        valid
        .groupBy("merchant_id", "country", "channel")
        .agg(
            count("*").alias("events"),
            spark_sum("amount").alias("total_amount"),
            avg("amount").alias("avg_amount"),
            avg("latency_seconds").alias("avg_latency_seconds"),
            spark_min("event_ts").alias("first_event_ts"),
            spark_max("event_ts").alias("last_event_ts"),
        )
        .withColumn("batch_id", lit(batch_id))
    )

    alerts = (
        valid
        .filter((col("amount") >= 800) | (col("latency_seconds") > 600))
        .withColumn(
            "alert_reason",
            when(col("amount") >= 800, lit("high_amount")).otherwise(lit("late_event")),
        )
        .select(
            "event_id",
            "event_ts",
            "processed_time",
            "customer_id",
            "merchant_id",
            "country",
            "channel",
            "amount",
            "latency_seconds",
            "alert_reason",
            "batch_id",
        )
    )

    valid.write.mode("append").parquet(f"{output_base}/silver_orders")
    invalid.write.mode("append").parquet(f"{output_base}/quarantine_orders")
    merchant_metrics.write.mode("append").parquet(f"{output_base}/merchant_metrics")
    alerts.write.mode("append").parquet(f"{output_base}/alerts")

    enriched_for_kafka = (
        valid
        .withColumn("value", to_json(struct(*[col(name) for name in valid.columns])))
        .selectExpr("CAST(event_id AS STRING) AS key", "CAST(value AS STRING) AS value")
    )
    enriched_for_kafka.write.format("kafka") \
        .option("kafka.bootstrap.servers", bootstrap_server) \
        .option("topic", enriched_topic) \
        .save()

    print(
        f"Batch {batch_id}: validos={valid.count()}, "
        f"invalidos={invalid.count()}, metricas={merchant_metrics.count()}, "
        f"alertas={alerts.count()}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bootstrap-server", default="kafka:9092")
    parser.add_argument("--input-topic", default="orders")
    parser.add_argument("--enriched-topic", default="orders_enriched")
    parser.add_argument("--output", default="/workspace/output")
    parser.add_argument("--checkpoint", default="/workspace/checkpoint/orders_stream")
    args = parser.parse_args()

    spark = build_spark()

    schema = StructType([
        StructField("event_id", StringType(), True),
        StructField("event_time", StringType(), True),
        StructField("source", StringType(), True),
        StructField("customer_id", StringType(), True),
        StructField("merchant_id", StringType(), True),
        StructField("country", StringType(), True),
        StructField("channel", StringType(), True),
        StructField("amount", DoubleType(), True),
        StructField("currency", StringType(), True),
        StructField("device_id", StringType(), True),
    ])

    raw = (
        spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", args.bootstrap_server)
        .option("subscribe", args.input_topic)
        .option("startingOffsets", "earliest")
        .option("failOnDataLoss", "true")
        .load()
    )

    parsed = (
        raw
        .selectExpr(
            "CAST(key AS STRING) AS kafka_key",
            "CAST(value AS STRING) AS raw_value",
            "topic",
            "partition",
            "offset",
            "timestamp AS kafka_timestamp",
        )
        .select(
            "kafka_key",
            "raw_value",
            "topic",
            "partition",
            "offset",
            "kafka_timestamp",
            from_json(col("raw_value"), schema).alias("event"),
        )
        .select("kafka_key", "raw_value", "topic", "partition", "offset", "kafka_timestamp", "event.*")
        .withColumn("event_ts", to_timestamp(col("event_time")))
        .withColumn("processed_time", current_timestamp())
        .withColumn("event_window_5m", window(col("event_ts"), "5 minutes"))
        .withColumn("event_date", expr("to_date(event_ts)"))
    )

    query = (
        parsed.writeStream
        .foreachBatch(
            lambda df, batch_id: process_batch(
                df,
                batch_id,
                args.output,
                args.bootstrap_server,
                args.enriched_topic,
            )
        )
        .option("checkpointLocation", args.checkpoint)
        .trigger(availableNow=True)
        .start()
    )

    query.awaitTermination()
    print("Consulta finalizada.")
    spark.stop()


if __name__ == "__main__":
    main()
