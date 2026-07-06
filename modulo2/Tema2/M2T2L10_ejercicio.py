from pyspark.sql import SparkSession

from pyspark.sql import functions as F

from pyspark.sql.window import Window

# Crear la sesión Spark

spark = SparkSession.builder \
    .appName("Top3SalariosPorDepartamento") \
    .master("local[*]") \
    .getOrCreate()

# Leer el fichero JSON

df = spark.read.json("empleados.json")

print("===== Primeros empleados =====")

df.show(5)

# Definir una ventana por departamento,

# ordenando los empleados por salario descendente

ventana = Window.partitionBy("departamento") \
                .orderBy(F.desc("salario"))

# Asignar un ranking dentro de cada departamento

top3 = (df
    .withColumn("ranking", F.row_number().over(ventana))
    .filter(F.col("ranking") <= 3)
    .select("departamento", "ranking", "nombre", "salario")
    .orderBy("departamento", "ranking")
)

print("\n===== Top 3 empleados con mayor salario por departamento =====")

top3.show(50, truncate=False)

spark.stop()