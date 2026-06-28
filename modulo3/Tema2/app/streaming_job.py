#!/usr/bin/env python3
import argparse

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    avg,
    col,
    count,
    current_timestamp,
    expr,
    length,
    lit,
    size,
    split,
    sum as spark_sum,
    to_timestamp,
    when,
)
from pyspark.sql.functions import from_json
from pyspark.sql.types import ArrayType, StringType, StructField, StructType


def process_batch(batch_df, batch_id: int, output_base: str):
    if batch_df.rdd.isEmpty():
        print(f"Batch {batch_id}: sin datos")
        return

    valid = (
        batch_df
        .filter(col("event_id").isNotNull())
        .filter(col("text").isNotNull())
        .filter(length(col("text")) > 0)
        .dropDuplicates(["event_id"])
        .withColumn("words", size(split(col("text"), " ")))
        .withColumn("length", length(col("text")))
        .withColumn("hashtag_count", size(col("hashtags")))
        .withColumn("mention_count", size(col("mentions")))
        .withColumn("unique_words", expr("size(array_distinct(split(lower(text), ' ')))"))
        .withColumn("batch_id", lit(batch_id))
    )

    invalid = (
        batch_df
        .filter(col("event_id").isNull() | col("text").isNull() | (length(col("text")) == 0))
        .withColumn(
            "error_reason",
            when(col("event_id").isNull(), lit("missing_event_id"))
            .when(col("text").isNull(), lit("missing_text"))
            .otherwise(lit("empty_text"))
        )
        .select("raw_value", "error_reason", "processed_time")
    )

    metrics = (
        valid
        .groupBy("source")
        .agg(
            count("*").alias("events"),
            avg("length").alias("avg_length"),
            avg("words").alias("avg_words"),
            spark_sum("hashtag_count").alias("hashtags"),
            spark_sum("mention_count").alias("mentions")
        )
        .withColumn("batch_id", lit(batch_id))
    )

    valid.write.mode("append").parquet(f"{output_base}/tweets_valid")
    invalid.write.mode("append").parquet(f"{output_base}/tweets_quarantine")
    metrics.write.mode("append").parquet(f"{output_base}/tweets_metrics")

    print(
        f"Batch {batch_id}: validos={valid.count()}, "
        f"invalidos={invalid.count()}, metricas={metrics.count()}"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bootstrap-server", default="kafka:9092")
    parser.add_argument("--topic", default="tweets")
    parser.add_argument("--output", default="/workspace/output")
    parser.add_argument("--checkpoint", default="/workspace/checkpoint/tweets_stream")
    args = parser.parse_args()

    spark = (
        SparkSession.builder
        .appName("M3T2KafkaSparkStructuredStreaming")
        .master("local[*]")
        .config("spark.sql.shuffle.partitions", "4")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")

    schema = StructType([
        StructField("event_id", StringType(), True),
        StructField("event_time", StringType(), True),
        StructField("source", StringType(), True),
        StructField("text", StringType(), True),
        StructField("hashtags", ArrayType(StringType()), True),
        StructField("mentions", ArrayType(StringType()), True),
    ])

    raw = (
        spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", args.bootstrap_server)
        .option("subscribe", args.topic)
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
            "timestamp AS kafka_timestamp"
        )
        .select(
            "kafka_key",
            "raw_value",
            "topic",
            "partition",
            "offset",
            "kafka_timestamp",
            from_json(col("raw_value"), schema).alias("event")
        )
        .select("kafka_key", "raw_value", "topic", "partition", "offset", "kafka_timestamp", "event.*")
        .withColumn("event_ts", to_timestamp(col("event_time")))
        .withColumn("processed_time", current_timestamp())
    )

    query = (
        parsed.writeStream
        .foreachBatch(lambda df, batch_id: process_batch(df, batch_id, args.output))
        .option("checkpointLocation", args.checkpoint)
        .trigger(availableNow=True)
        .start()
    )

    query.awaitTermination()
    print("Consulta finalizada.")


if __name__ == "__main__":
    main()
