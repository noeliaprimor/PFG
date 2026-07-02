import os
import shutil

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, count, max, min, window
from pyspark.sql.types import DoubleType, StringType, StructField, StructType, TimestampType


INPUT_DIR = os.path.abspath("input/crypto_prices")
OUTPUT_DIR = os.path.abspath("output/crypto_prices_parquet")
CHECKPOINT_DIR = os.path.abspath("checkpoint/crypto_prices")


def prepare_directories():
    for path in (INPUT_DIR, OUTPUT_DIR, CHECKPOINT_DIR):
        shutil.rmtree(path, ignore_errors=True)
        os.makedirs(path, exist_ok=True)

    print("Directorio de trabajo:", os.getcwd())
    print("Carpetas preparadas y limpiadas:")
    print("-", INPUT_DIR)
    print("-", OUTPUT_DIR)
    print("-", CHECKPOINT_DIR)


def create_spark_session():
    spark = (
        SparkSession.builder
        .appName("CoinGeckoFileStreaming")
        .master("local[*]")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")
    return spark


def main():
    prepare_directories()
    spark = create_spark_session()

    schema = StructType([
        StructField("event_time", TimestampType(), True),
        StructField("coin", StringType(), True),
        StructField("currency", StringType(), True),
        StructField("price", DoubleType(), True),
    ])

    stream_df = (
        spark.readStream
        .schema(schema)
        .option("timestampFormat", "yyyy-MM-dd'T'HH:mm:ss'Z'")
        .json(INPUT_DIR)
    )
    stream_df.printSchema()

    raw_query = (
        stream_df.writeStream
        .format("console")
        .option("checkpointLocation", os.path.join(CHECKPOINT_DIR, "raw_console"))
        .outputMode("append")
        .option("truncate", "false")
        .trigger(availableNow=True)
        .start()
    )
    raw_query.awaitTermination()

    metrics_df = (
        stream_df
        .withWatermark("event_time", "1 minute")
        .groupBy(window(col("event_time"), "1 minute"), col("coin"))
        .agg(
            avg("price").alias("avg_price"),
            max("price").alias("max_price"),
            min("price").alias("min_price"),
            count("*").alias("num_events"),
        )
    )
    metrics_df.printSchema()

    metrics_query = (
        metrics_df.writeStream
        .option("checkpointLocation", os.path.join(CHECKPOINT_DIR, "metrics_console"))
        .outputMode("complete")
        .format("console")
        .option("truncate", "false")
        .trigger(availableNow=True)
        .start()
    )
    metrics_query.awaitTermination()

    parquet_query = (
        stream_df.writeStream
        .format("parquet")
        .option("path", OUTPUT_DIR)
        .option("checkpointLocation", os.path.join(CHECKPOINT_DIR, "parquet"))
        .outputMode("append")
        .trigger(availableNow=True)
        .start()
    )
    parquet_query.awaitTermination()

    historical_df = spark.read.parquet(OUTPUT_DIR)
    historical_df.show(truncate=False)
    historical_df.groupBy("coin").count().show()

    for query in spark.streams.active:
        print("Deteniendo consulta:", query.name, query.id)
        query.stop()

    print("Consultas activas:", spark.streams.active)
    spark.stop()


if __name__ == "__main__":
    main()
