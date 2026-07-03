from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

spark = (SparkSession.builder
         .appName("AdquisicionEventos")
         .master("local[*]")
         .getOrCreate())

datos = [
    ('{"event_id":"evt-001","event_type":"pedido_creado","event_time":"2026-07-03T10:00:00Z","key":"pedido-1","payload":{"cliente_id":"cli-1","importe":25.5,"moneda":"EUR"}}',),
    ('{"event_id":"evt-002","event_type":"pedido_creado","event_time":"2026-07-03T10:01:00Z","key":"pedido-2","payload":{"cliente_id":"cli-2","importe":40.0,"moneda":"EUR"}}',),
    ('{"event_id":"evt-003","event_type":"pedido_creado","event_time":null,"key":"pedido-3","payload":{"cliente_id":"cli-3","importe":15.0,"moneda":"EUR"}}',),
    ('{"event_id":"evt-004","event_type":"pedido_creado","event_time":"2026-07-03T10:03:00Z","key":null,"payload":{"cliente_id":"cli-4","importe":18.5,"moneda":"EUR"}}',)
]

df_raw = spark.createDataFrame(datos, ["json_event"])

schema = StructType([
    StructField("event_id", StringType()),
    StructField("event_type", StringType()),
    StructField("event_time", StringType()),
    StructField("key", StringType()),
    StructField("payload", StructType([
        StructField("cliente_id", StringType()),
        StructField("importe", DoubleType()),
        StructField("moneda", StringType())
    ]))
])

eventos = (df_raw
           .select(F.from_json(F.col("json_event"), schema).alias("evento"))
           .select("evento.*"))

eventos_validados = eventos.withColumn(
    "estado",
    F.when(
        F.col("event_id").isNotNull() &
        F.col("event_type").isNotNull() &
        F.col("event_time").isNotNull() &
        F.col("key").isNotNull() &
        F.col("payload.cliente_id").isNotNull() &
        F.col("payload.importe").isNotNull(),
        "valido"
    ).otherwise("invalido")
)

eventos_validados.select(
    "event_id",
    "event_type",
    "event_time",
    "key",
    "payload.cliente_id",
    "payload.importe",
    "payload.moneda",
    "estado"
).show(truncate=False)

spark.stop()