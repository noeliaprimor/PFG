from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (SparkSession.builder
         .appName("IoTStreaming")
         .master("local[*]")
         .getOrCreate())

eventos = (spark.readStream
           .format("rate")
           .option("rowsPerSecond", 9)
           .load())

eventos = eventos.withColumn(
    "sensor_id",
    F.concat(
        F.lit("sensor_"),
        (F.col("value") % 3 + 1).cast("string")
    )
)

resultado = (
    eventos
    .groupBy(
        F.window("timestamp", "15 seconds"),
        "sensor_id"
    )
    .count()
)

query = (
    resultado.writeStream
    .outputMode("complete")
    .format("console")
    .option("truncate", "false")
    .start()
)

query.awaitTermination()