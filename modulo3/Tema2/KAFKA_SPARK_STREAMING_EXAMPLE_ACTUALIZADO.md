# Kafka + Spark Streaming Example actualizado

Actualizacion operativa del repositorio:

<https://github.com/dbusteed/kafka-spark-streaming-example>

El ejemplo original tiene varios años y usa piezas que hoy no son la opcion mas recomendable para un laboratorio nuevo: ZooKeeper, Spark Streaming clasico con Kafka 0.8, Hive local y una instalacion manual larga sobre una VM. Esta version mantiene la idea didactica del proyecto original, pero la actualiza a un entorno reproducible con Docker Compose, Kafka en modo KRaft y Spark Structured Streaming.

## Objetivo

Construir un pipeline completo:

1. Un productor Python genera eventos tipo tweet en JSON.
2. Los eventos se publican en un topic Kafka llamado `tweets`.
3. Spark Structured Streaming consume el topic.
4. Spark valida y transforma los eventos.
5. Los resultados validos se escriben en Parquet.
6. Los eventos invalidos se escriben en una zona de cuarentena.
7. Se generan metricas por microbatch para comprobar el procesamiento.

## Cambios respecto al ejemplo original

| Aspecto | Ejemplo original | Version actualizada |
|---|---|---|
| Kafka | Kafka + ZooKeeper | Kafka 4.2 en modo KRaft |
| Spark | Spark Streaming clasico / DStreams | Spark Structured Streaming |
| Integracion Kafka | `spark-streaming-kafka-0-8` | `spark-sql-kafka-0-10` |
| Sink | Hive textfile | Parquet local |
| Instalacion | Manual en VM | Docker Compose |
| Productor | Tweets reales o texto simulado | Eventos JSON simulados |
| Validacion | Minima | Validos, invalidos y metricas |
| Reproducibilidad | Depende de VM y versiones antiguas | Versiones fijadas y comandos reproducibles |

## Referencias oficiales

- Kafka Quickstart y Docker: <https://kafka.apache.org/quickstart>
- Imagen Docker oficial de Kafka: <https://kafka.apache.org/42/getting-started/docker/>
- Spark Structured Streaming + Kafka: <https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html>

## Guia paso a paso desde cero

Esta seccion esta pensada para ejecutar el ejercicio aunque no tengas experiencia DevOps. La idea es no instalar Kafka ni Spark directamente en tu maquina, sino usar Docker para levantar todo de forma controlada.

Los pasos estan escritos para Ubuntu/Debian. Si usas Windows o macOS, instala Docker Desktop, abre una terminal y empieza en el apartado "Crear el laboratorio".

### 0. Instalar herramientas basicas en Ubuntu/Debian

Actualiza paquetes:

```bash
sudo apt update
sudo apt upgrade -y
```

Instala Git, curl y certificados:

```bash
sudo apt install -y git curl ca-certificates
```

Instala Docker desde el repositorio oficial:

```bash
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

Anade el repositorio de Docker:

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Instala Docker Engine y Docker Compose:

```bash
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Permite usar Docker sin `sudo`:

```bash
sudo usermod -aG docker "$USER"
```

Cierra sesion y vuelve a entrar. Si estas en una terminal remota, sal y vuelve a conectarte. Despues comprueba:

```bash
docker --version
docker compose version
docker run --rm hello-world
```

Si `hello-world` termina correctamente, Docker esta listo.

### 1. Crear el laboratorio

Crea una carpeta limpia:

```bash
mkdir -p ~/m3t2-kafka-spark-lab
cd ~/m3t2-kafka-spark-lab
```

Genera todos los ficheros del laboratorio con este script:

```bash
cat > crear_laboratorio.sh <<'SCRIPT'
#!/usr/bin/env bash
set -euo pipefail

mkdir -p app output checkpoint

cat > docker-compose.yml <<'EOF'
services:
  kafka:
    image: apache/kafka:4.2.0
    container_name: m3t2-kafka
    hostname: kafka
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
SCRIPT

chmod +x crear_laboratorio.sh
./crear_laboratorio.sh
```

Si el comando termina con `Laboratorio creado correctamente.`, ya tienes todos los ficheros necesarios.

### 2. Construir la imagen del laboratorio

Este paso descarga Python, Java y las dependencias de PySpark. La primera vez puede tardar varios minutos:

```bash
docker compose build
```

Resultado esperado: debe terminar sin errores y mostrar algo similar a `Successfully built` o `DONE`.

### 3. Arrancar Kafka

```bash
docker compose up -d kafka
```

Comprueba el estado:

```bash
docker compose ps
```

Espera hasta que `kafka` aparezca como `healthy`. Si aun esta arrancando, espera unos segundos y repite:

```bash
docker compose ps
```

### 4. Crear el topic `tweets`

```bash
docker compose exec kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server kafka:9092 \
  --create \
  --if-not-exists \
  --topic tweets \
  --partitions 3 \
  --replication-factor 1
```

Comprueba que existe:

```bash
docker compose exec kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server kafka:9092 \
  --describe \
  --topic tweets
```

Resultado esperado: debe aparecer `PartitionCount: 3`.

### 5. Producir eventos JSON en Kafka

```bash
docker compose run --rm lab \
  python /workspace/app/producer_json.py \
  --bootstrap-server kafka:9092 \
  --topic tweets \
  --messages 300 \
  --sleep 0.01
```

Resultado esperado:

```text
Eventos enviados: 25
Eventos enviados: 50
...
Finalizado. Total eventos enviados: 300
```

### 6. Ver algunos mensajes en Kafka

```bash
docker compose exec kafka /opt/kafka/bin/kafka-console-consumer.sh \
  --bootstrap-server kafka:9092 \
  --topic tweets \
  --from-beginning \
  --max-messages 5
```

Resultado esperado: deben verse 5 mensajes JSON con campos como `event_id`, `event_time`, `source` y `text`.

### 7. Ejecutar Spark Structured Streaming

```bash
docker compose run --rm lab \
  spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
  /workspace/app/streaming_job.py \
  --bootstrap-server kafka:9092 \
  --topic tweets \
  --output /workspace/output \
  --checkpoint /workspace/checkpoint/tweets_stream
```

La primera ejecucion puede tardar porque Spark descarga el conector Kafka desde Maven.

Resultado esperado:

```text
Batch 0: validos=300, invalidos=0, metricas=1
Consulta finalizada.
```

El numero exacto de batches puede variar. Lo importante es que aparezcan registros validos.

### 8. Validar los resultados

```bash
docker compose run --rm lab \
  python /workspace/app/validate_outputs.py
```

Resultado esperado:

```text
== tweets_valid ==
Registros: 300

== tweets_quarantine ==
Registros: 0

== tweets_metrics ==
Registros: 1
```

Tambien puedes comprobar los ficheros en tu maquina:

```bash
find output -maxdepth 3 -type f | sort
find checkpoint -maxdepth 3 -type f | sort
```

### 9. Repetir el ejercicio desde cero

Si quieres limpiar resultados y volver a ejecutar:

```bash
rm -rf output/* checkpoint/*
```

Vuelve a producir eventos:

```bash
docker compose run --rm lab \
  python /workspace/app/producer_json.py \
  --bootstrap-server kafka:9092 \
  --topic tweets \
  --messages 100 \
  --sleep 0.01
```

Vuelve a ejecutar Spark:

```bash
docker compose run --rm lab \
  spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
  /workspace/app/streaming_job.py \
  --bootstrap-server kafka:9092 \
  --topic tweets \
  --output /workspace/output \
  --checkpoint /workspace/checkpoint/tweets_stream
```

### 10. Parar todo

Para parar contenedores:

```bash
docker compose down
```

Para borrar tambien volumenes internos:

```bash
docker compose down -v
```

### 11. Checklist rapido

Antes de pedir ayuda, comprueba:

```bash
docker compose ps
docker compose logs kafka --tail=50
find output -maxdepth 3 -type f
find checkpoint -maxdepth 3 -type f
```

Si Kafka no esta `healthy`, el problema esta en el arranque de Kafka. Si Kafka esta bien pero no hay salida, revisa que el productor haya enviado eventos y que Spark haya terminado sin errores.


## 11. Ejecucion continua opcional

Para observar comportamiento continuo:

Terminal 1:

```bash
docker compose run --rm lab \
  spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
  /workspace/app/streaming_job.py \
  --bootstrap-server kafka:9092 \
  --topic tweets \
  --output /workspace/output \
  --checkpoint /workspace/checkpoint/tweets_stream
```

Terminal 2:

```bash
docker compose run --rm lab \
  python /workspace/app/producer_json.py \
  --bootstrap-server kafka:9092 \
  --topic tweets \
  --messages 1000 \
  --sleep 0.1
```

Para una consulta verdaderamente infinita, cambia en `streaming_job.py`:

```python
.trigger(availableNow=True)
```

por:

```python
.trigger(processingTime="10 seconds")
```

## 12. Limpieza

Parar contenedores:

```bash
docker compose down
```

Reiniciar resultados y checkpoints:

```bash
rm -rf output/* checkpoint/*
```

Eliminar tambien datos internos de Kafka:

```bash
docker compose down -v
```

## 13. Ejercicios de mejora

### Ejercicio 1: latencia extremo a extremo

Calcula la diferencia entre `event_ts` y `processed_time`.

Pistas:

```python
from pyspark.sql.functions import unix_timestamp

latency_seconds = unix_timestamp("processed_time") - unix_timestamp("event_ts")
```

Guarda media, minimo y maximo por microbatch.

### Ejercicio 2: particionado

Ejecuta dos pruebas:

1. Topic con 1 particion.
2. Topic con 3 particiones.

Compara:

- tiempo total de procesamiento;
- distribucion de offsets;
- numero de ficheros generados;
- efecto sobre paralelismo.

### Ejercicio 3: eventos invalidos

Modifica el productor para generar un 5% de mensajes invalidos:

- sin `event_id`;
- sin `text`;
- JSON mal formado.

Comprueba que aparecen en `output/tweets_quarantine`.

### Ejercicio 4: salida agregada por ventana

Anade una salida de metricas por ventana de evento:

- ventana de 1 minuto;
- total de eventos;
- longitud media;
- total de hashtags;
- total de menciones.

### Ejercicio 5: migracion conceptual desde el repo original

Documenta que partes del repositorio original se han sustituido:

- ZooKeeper por KRaft.
- Spark Streaming clasico por Structured Streaming.
- Hive textfile por Parquet.
- texto plano por JSON con esquema.
- ejecucion manual en VM por Docker Compose.

### Ejercicio 6: sink alternativo

Anade escritura a otro topic Kafka llamado `tweets_enriched`.

Pista:

```python
from pyspark.sql.functions import to_json, struct

out = valid.selectExpr("CAST(event_id AS STRING) AS key") \
    .withColumn("value", to_json(struct("*"))) \
    .select("key", "value")
```

Despues escribe con:

```python
.writeStream.format("kafka")
```

### Ejercicio 7: idempotencia

Ejecuta dos veces el job con el mismo checkpoint y comprueba que no reprocesa los mismos offsets.

Despues borra `checkpoint/` y ejecuta otra vez. Explica que ocurre y por que.

## 14. Problemas frecuentes

### Kafka no esta listo

Espera a que el healthcheck termine:

```bash
docker compose ps
```

### `UnknownHostException: kafka`

Estas ejecutando Spark fuera de Docker. Si ejecutas en host, usa `localhost:9092` y ajusta `KAFKA_ADVERTISED_LISTENERS`. La guia esta pensada para ejecutar productor y Spark dentro del servicio `lab`.

### Error descargando paquetes Maven

El primer `spark-submit --packages` necesita internet para descargar el conector Spark-Kafka. Repite cuando haya red o configura un repositorio Maven interno.

### No aparecen nuevos datos

Si usas el mismo checkpoint, Spark continua desde el ultimo offset procesado. Para una prueba desde cero:

```bash
rm -rf checkpoint/* output/*
```

### Hay muchos ficheros pequenos

Es normal en laboratorios con microbatches. En produccion se ajustan particiones, frecuencia de trigger y procesos de compactacion.

## 15. Resultado esperado

Tras ejecutar los pasos principales, `validate_outputs.py` debe mostrar:

- registros validos en `tweets_valid`;
- cero o mas registros invalidos en `tweets_quarantine`;
- metricas por `source` en `tweets_metrics`.

Ejemplo de salida esperada:

```text
== tweets_valid ==
Registros: 300

== tweets_quarantine ==
Registros: 0

== tweets_metrics ==
Registros: 1
```

## 16. Por que esta version es mas actual

- Usa Kafka en modo KRaft, alineado con las versiones actuales de Kafka.
- Usa Spark Structured Streaming, la API recomendada para nuevos desarrollos.
- Usa el conector `spark-sql-kafka-0-10`, no el antiguo `spark-streaming-kafka-0-8`.
- Usa JSON con esquema explicito.
- Usa Parquet como sink analitico portable.
- Usa Docker Compose para reproducibilidad.
- Elimina dependencias manuales largas de Hadoop/Hive para un primer laboratorio.
