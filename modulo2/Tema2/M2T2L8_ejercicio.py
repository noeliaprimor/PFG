from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Operaciones sobre RDD") \
    .getOrCreate()

# Leer el JSON
df = spark.read.json("empleados.json")

# Convertir a RDD
rdd = df.rdd

print("===== Empleados =====")
print(rdd.take(5))

# -------------------------
# 1. MAP
# -------------------------

print("\n===== Nombres =====")

nombres = rdd.map(lambda fila: fila.nombre)

print(nombres.take(5))

# -------------------------
# 2. FILTER
# -------------------------

print("\n===== Empleados IT =====")

it = rdd.filter(lambda fila: fila.departamento == "IT")

print(it.take(5))

# -------------------------
# 3. MAP
# -------------------------

print("\n===== Salario con incremento del 10% =====")

salarios = rdd.map(
    lambda fila: (fila.nombre, fila.salario * 1.10)
)

print(salarios.take(5))

# -------------------------
# 4. MAP + REDUCEBYKEY
# -------------------------

print("\n===== Número de empleados por departamento =====")

conteo = (rdd
          .map(lambda fila: (fila.departamento, 1))
          .reduceByKey(lambda a, b: a + b))

print(conteo.collect())

# -------------------------
# 5. MAP + REDUCEBYKEY
# -------------------------

print("\n===== Salario total por departamento =====")

salario_total = (rdd
                 .map(lambda fila: (fila.departamento, fila.salario))
                 .reduceByKey(lambda a, b: a + b))

print(salario_total.collect())

spark.stop()