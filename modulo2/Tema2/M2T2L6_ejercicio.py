from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("RDD Empleados") \
    .getOrCreate()

# Leer el JSON

df = spark.read.json("empleados.json")


# Convertir el DataFrame en RDD

rdd = df.rdd

print("Contenido del RDD:")

print(rdd.take(3))

# Obtener únicamente el departamento

departamentos = rdd.map(lambda fila: fila.departamento)

# Crear pares (departamento,1)

pares = departamentos.map(lambda d: (d, 1))

# Contar empleados por departamento

conteo = pares.reduceByKey(lambda a, b: a + b)

print("Número de empleados por departamento:")

print(conteo.collect())

spark.stop()