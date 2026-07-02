from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("JSON a Parquet") \
    .getOrCreate()

# Leer el JSON
df = spark.read.json("empleados.json")
print("Esquema:")

df.printSchema()
print("Datos:")

df.show()

# Guardar en formato Parquet

df.write.mode("overwrite").parquet("empleados_parquet")

print("Fichero Parquet creado correctamente.")

# Leer el Parquet para comprobarlo

df_parquet = spark.read.parquet("empleados_parquet")

print("Contenido del Parquet:")

df_parquet.show()

spark.stop()