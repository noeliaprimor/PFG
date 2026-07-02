from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Particionado por departamento") \
    .getOrCreate()

# Leer JSON
df = spark.read.json("empleados.json")

print("Datos originales:")
df.show()

# Guardar en Parquet particionado por departamento
df.write \
    .mode("overwrite") \
    .partitionBy("departamento") \
    .parquet("empleados_particionado")

print("Datos guardados en empleados_particionado/")

# Leer de nuevo el Parquet
df_particionado = spark.read.parquet("empleados_particionado")

print("Datos leídos desde Parquet particionado:")
df_particionado.show()

spark.stop()