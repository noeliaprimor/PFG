#!/usr/bin/env bash
set -euo pipefail

mkdir -p app output checkpoint

cat > docker-compose.yml <<'EOF'
services:
  kafka:
    image: apache/kafka:4.2.0
    container_name: m3t2-kafka
    ports:
      - "9092:9092"
    environment:
      KAFKA_NODE_ID: 1
      KAFKA_PROCESS_ROLES: broker,controller
      KAFKA_LISTENERS: PLAINTEXT://:9092,CONTROLLER://:9093
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092
      KAFKA_CONTROLLER_LISTENER_NAMES: CONTROLLER
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT
      KAFKA_CONTROLLER_QUORUM_VOTERS: 1@kafka:9093
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: 1
      KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: 1
      KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS: 0
      KAFKA_NUM_PARTITIONS: 3
    healthcheck:
      test: [ "CMD", "/opt/kafka/bin/kafka-topics.sh", "--bootstrap-server", "kafka:9092", "--list" ]
      interval: 10s
      timeout: 10s
      retries: 10

  lab:
    build: .
    container_name: m3t2-spark-lab
    depends_on:
      kafka:
        condition: service_healthy
    volumes:
      - ./app:/workspace/app
      - ./output:/workspace/output
      - ./checkpoint:/workspace/checkpoint
    working_dir: /workspace
    environment:
      PYSPARK_PYTHON: python3
      PYSPARK_DRIVER_PYTHON: python3
EOF

cat > Dockerfile <<'EOF'
FROM python:3.11-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends openjdk-17-jre-headless curl procps \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3

WORKDIR /workspace

COPY requirements.txt /workspace/requirements.txt
RUN pip install --no-cache-dir -r /workspace/requirements.txt
EOF

cat > requirements.txt <<'EOF'
pyspark==3.5.1
kafka-python==2.0.2
EOF

cat > app/producer_json.py <<'EOF'
#!/usr/bin/env python3
import argparse
import json
import random
import time
import uuid
from datetime import datetime, timezone

from kafka import KafkaProducer


WORDS = [
    "spark", "kafka", "streaming", "data", "pipeline", "python",
    "latency", "checkpoint", "topic", "producer", "consumer", "parquet",
    "analytics", "event", "window", "watermark"
]
HASHTAGS = ["#bigdata", "#spark", "#kafka", "#streaming", "#python"]
MENTIONS = ["@data_team", "@spark_user", "@kafka_lab"]


def build_event(source: str) -> dict:
    tokens = random.choices(WORDS, k=random.randint(6, 16))

    if random.random() < 0.75:
        tokens.append(random.choice(HASHTAGS))
    if random.random() < 0.45:
        tokens.append(random.choice(MENTIONS))

    text = " ".join(tokens)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    return {
        "event_id": str(uuid.uuid4()),
        "event_time": now,
        "source": source,
        "text": text,
        "hashtags": [token for token in tokens if token.startswith("#")],
        "mentions": [token for token in tokens if token.startswith("@")]
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bootstrap-server", default="kafka:9092")
    parser.add_argument("--topic", default="tweets")
    parser.add_argument("--messages", type=int, default=200)
    parser.add_argument("--sleep", type=float, default=0.05)
    parser.add_argument("--source", default="m3t2-json-producer")
    args = parser.parse_args()

    producer = KafkaProducer(
        bootstrap_servers=args.bootstrap_server,
        key_serializer=lambda value: value.encode("utf-8"),
        value_serializer=lambda value: json.dumps(value).encode("utf-8"),
        acks="all",
        retries=5
    )

    for i in range(args.messages):
        event = build_event(args.source)
        producer.send(args.topic, key=event["event_id"], value=event)
        if (i + 1) % 25 == 0:
            producer.flush()
            print(f"Eventos enviados: {i + 1}")
        time.sleep(args.sleep)

    producer.flush()
    producer.close()
    print(f"Finalizado. Total eventos enviados: {args.messages}")


if __name__ == "__main__":
    main()
EOF

cat > app/streaming_job.py <<'EOF'
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
EOF

cat > app/validate_outputs.py <<'EOF'
#!/usr/bin/env python3
from pathlib import Path

from pyspark.sql import SparkSession


OUTPUT = Path("/workspace/output")

spark = (
    SparkSession.builder
    .appName("M3T2ValidateOutputs")
    .master("local[*]")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("WARN")

for name in ["tweets_valid", "tweets_quarantine", "tweets_metrics"]:
    path = OUTPUT / name
    print(f"\n== {name} ==")
    if not path.exists():
        print("No existe:", path)
        continue

    df = spark.read.parquet(str(path))
    print("Registros:", df.count())
    df.show(10, truncate=False)

spark.stop()
EOF

chmod +x app/*.py

echo "Laboratorio creado correctamente."
echo "Ficheros:"
find . -maxdepth 3 -type f | sort
