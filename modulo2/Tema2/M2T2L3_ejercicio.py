from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder \
    .appName("M2T2L3_ejercicio") \
    .master("local[*]") \
    .getOrCreate()

sc = spark.sparkContext

# RDD
rdd = sc.parallelize(range(1, 101))
suma = rdd.reduce(lambda a, b: a + b)
print("Suma:", suma)

# DataFrame
df = spark.createDataFrame([(i,) for i in range(1, 101)], ["numero"])
media = df.select(avg("numero")).collect()
print("Media:", media)

spark.stop()