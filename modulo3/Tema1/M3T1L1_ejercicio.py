from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = (
    SparkSession.builder
    .appName("StreamingValoracionesPeliculas")
    .master("local[*]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

schema = StructType([
    StructField("pelicula", StringType(), True),
    StructField("usuario", StringType(), True),
    StructField("valoracion", IntegerType(), True)
])

valoraciones = (
    spark.readStream
    .option("header", True)
    .schema(schema)
    .csv("entrada_valoraciones")
)

metricas = (
    valoraciones
    .groupBy("pelicula")
    .agg(
        F.count("*").alias("num_valoraciones"),
        F.round(F.avg("valoracion"), 2).alias("valoracion_media")
    )
)

query = (
    metricas.writeStream
    .outputMode("complete")
    .format("console")
    .option("truncate", False)
    .option("checkpointLocation", "checkpoint_m3t1l1")
    .trigger(processingTime="10 seconds")
    .start()
)

query.awaitTermination(60)

query.stop()
spark.stop()