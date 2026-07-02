from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("EjercicioSparkSubmit") \
    .getOrCreate()

datos = [("A", 10), ("B", 20), ("A", 15)]
df = spark.createDataFrame(datos, ["grupo", "valor"])
resultado = df.groupBy("grupo").sum("valor")

resultado.show()
spark.stop()
