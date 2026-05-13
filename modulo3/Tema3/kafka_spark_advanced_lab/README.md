# M3T3 ejercicio avanzado: Kafka + Spark Structured Streaming

Laboratorio autocontenido para ejecutar un pipeline de streaming con Kafka y Spark.

## Flujo

1. `producer_orders.py` genera eventos de pedidos/transacciones en JSON.
2. Kafka recibe los eventos en el topic `orders`.
3. `streaming_pipeline.py` consume Kafka con Spark Structured Streaming.
4. El job valida eventos, calcula latencia, métricas por comercio y alertas.
5. Los resultados se guardan en Parquet y los eventos enriquecidos se publican en `orders_enriched`.

## Ejecución rápida

```bash
docker compose build
docker compose up -d kafka
docker compose exec kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server kafka:9092 --create --if-not-exists --topic orders --partitions 3 --replication-factor 1
docker compose exec kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server kafka:9092 --create --if-not-exists --topic orders_enriched --partitions 3 --replication-factor 1
docker compose run --rm lab python /workspace/app/producer_orders.py --bootstrap-server kafka:9092 --topic orders --messages 1000 --sleep 0.01
docker compose run --rm lab spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 /workspace/app/streaming_pipeline.py --bootstrap-server kafka:9092 --input-topic orders --enriched-topic orders_enriched --output /workspace/output --checkpoint /workspace/checkpoint/orders_stream
docker compose run --rm lab python /workspace/app/validate_outputs.py
```
