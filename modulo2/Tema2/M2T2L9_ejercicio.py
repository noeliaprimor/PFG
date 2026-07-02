from pyspark.sql import SparkSession
from pyspark.sql.functions import count, avg, round

spark = SparkSession.builder \
    .appName("DataFrame Empleados") \
    .getOrCreate()

# 1. Crear un DataFrame leyendo el JSON
df = spark.read.json("empleados.json")

print("===== Esquema =====")
df.printSchema()

print("===== Primeros empleados =====")
df.show(10, truncate=False)

# 2. Filtrar salarios altos
salarios_altos = df.filter(df.salario >= 45000)

print("===== Empleados con salario alto =====")
salarios_altos.show(10, truncate=False)

# 3. Agrupar por departamento
resumen = df.groupBy("departamento") \
    .agg(
        count("*").alias("numero_empleados"),
        round(avg("salario"), 2).alias("salario_medio")
    ) \
    .orderBy("departamento")

print("===== Resumen por departamento =====")
resumen.show(truncate=False)

spark.stop()