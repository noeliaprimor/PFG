from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("StreamingPeliculas")
    .master("local[*]")
    .getOrCreate()
)

stream = (
    spark.readStream
         .format("rate")
         .option("rowsPerSecond", 5)
         .load()
)

peliculas = (
    stream
    .withColumn(
        "pelicula",
        F.when(F.col("value") % 10 == 0, "Matrix")
        .when(F.col("value") % 10 == 1, "Interstellar")
        .when(F.col("value") % 10 == 2, "Inception")
        .when(F.col("value") % 10 == 3, "El Padrino")
        .when(F.col("value") % 10 == 4, "Pulp Fiction")
        .when(F.col("value") % 10 == 5, "El Caballero Oscuro")
        .when(F.col("value") % 10 == 6, "Forrest Gump")
        .when(F.col("value") % 10 == 7, "Titanic")
        .when(F.col("value") % 10 == 8, "Gladiator")
        .otherwise("Avatar")
    )
    .withColumn(
        "valoracion",
        (F.col("value") % 5) + 1
    )
)

estadisticas = (
    peliculas
    .groupBy(
        F.window("timestamp", "15 seconds"),
        "pelicula"
    )
    .agg(
        F.count("*").alias("num_valoraciones"),
        F.avg("valoracion").alias("media")
    )
)

query = (
    estadisticas
    .writeStream
    .outputMode("complete")
    .format("console")
    .start()
)

query.awaitTermination()