#!/usr/bin/env python3
import argparse
import json
import random
import time
import uuid
from datetime import datetime, timedelta, timezone

from kafka import KafkaProducer


COUNTRIES = ["ES", "FR", "DE", "IT", "PT", "NL"]
CHANNELS = ["web", "mobile", "pos", "api"]
MERCHANTS = ["m-100", "m-200", "m-300", "m-400", "m-500"]
CUSTOMERS = [f"c-{i:04d}" for i in range(1, 501)]


def utc_now_iso(offset_seconds: int = 0) -> str:
    value = datetime.now(timezone.utc) + timedelta(seconds=offset_seconds)
    return value.strftime("%Y-%m-%dT%H:%M:%SZ")


def build_order(source: str, late_probability: float) -> dict:
    amount = round(random.expovariate(1 / 55) + random.uniform(2, 30), 2)
    if random.random() < 0.03:
        amount = round(random.uniform(800, 2500), 2)

    event_delay = 0
    if random.random() < late_probability:
        event_delay = -random.randint(360, 1800)

    return {
        "event_id": str(uuid.uuid4()),
        "event_time": utc_now_iso(event_delay),
        "source": source,
        "customer_id": random.choice(CUSTOMERS),
        "merchant_id": random.choice(MERCHANTS),
        "country": random.choice(COUNTRIES),
        "channel": random.choice(CHANNELS),
        "amount": amount,
        "currency": "EUR",
        "device_id": f"d-{random.randint(1, 180):04d}",
    }


def build_invalid_message() -> str:
    option = random.choice(["bad_json", "missing_event_id", "missing_amount", "negative_amount"])
    if option == "bad_json":
        return '{"event_id": "broken", "amount": '

    event = build_order("invalid-generator", late_probability=0.0)
    if option == "missing_event_id":
        event.pop("event_id")
    elif option == "missing_amount":
        event.pop("amount")
    elif option == "negative_amount":
        event["amount"] = -10
    return json.dumps(event)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bootstrap-server", default="kafka:9092")
    parser.add_argument("--topic", default="orders")
    parser.add_argument("--messages", type=int, default=1000)
    parser.add_argument("--sleep", type=float, default=0.02)
    parser.add_argument("--source", default="orders-simulator")
    parser.add_argument("--invalid-rate", type=float, default=0.03)
    parser.add_argument("--late-rate", type=float, default=0.08)
    args = parser.parse_args()

    producer = KafkaProducer(
        bootstrap_servers=args.bootstrap_server,
        key_serializer=lambda value: value.encode("utf-8"),
        value_serializer=lambda value: value.encode("utf-8"),
        acks="all",
        retries=5,
    )

    for index in range(args.messages):
        if random.random() < args.invalid_rate:
            key = str(uuid.uuid4())
            payload = build_invalid_message()
        else:
            event = build_order(args.source, args.late_rate)
            key = event["event_id"]
            payload = json.dumps(event)

        producer.send(args.topic, key=key, value=payload)
        if (index + 1) % 100 == 0:
            producer.flush()
            print(f"Eventos enviados: {index + 1}")
        time.sleep(args.sleep)

    producer.flush()
    producer.close()
    print(f"Finalizado. Total eventos enviados: {args.messages}")


if __name__ == "__main__":
    main()
