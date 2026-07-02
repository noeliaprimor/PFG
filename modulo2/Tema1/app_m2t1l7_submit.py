
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark import SparkFiles
from time import time

spark = SparkSession.builder.appName("M2T1L7_spark_submit_demo").getOrCreate()

inicio = time()
df = spark.read.csv(SparkFiles.get("heart.csv"), header=True, inferSchema=True)

resultado = (df
    .filter(F.col("Age") >= 50)
    .groupBy("Age")
    .agg(
        F.count("*").alias("registros"),
        F.avg("Cholesterol").alias("colesterol_medio"),
        F.avg("BP").alias("bp_media")
    )
    .orderBy("Age"))

resultado.show(50, truncate=False)
print("Filas procesadas:", df.count())
print("Particiones:", df.rdd.getNumPartitions())
print("Tiempo total:", round(time() - inicio, 2), "segundos")

spark.stop()
