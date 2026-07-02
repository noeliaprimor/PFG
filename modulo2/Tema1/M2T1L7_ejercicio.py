from pyspark.sql import SparkSession
from pyspark.sql.functions import count, avg

spark = SparkSession.builder.appName("M2T1L7 Heart Submit").getOrCreate()

df = spark.read.csv(
    "heart.csv",
    header=True,
    inferSchema=True
)

print("Total de registros:")
print(df.count())
print("Agrupación por edad:")

resultado = df.groupBy("Age") \
    .agg(
        count("*").alias("num_registros"),
        avg("Cholesterol").alias("colesterol_medio")
    ) \
    .orderBy("Age")

resultado.show()

