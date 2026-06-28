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
