from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SparkSQLEmpleados") \
    .master("local[*]") \
    .getOrCreate()

# Leer JSON

df = spark.read.json("empleados.json")

# Registrar vista temporal

df.createOrReplaceTempView("empleados")
consulta = """
SELECT
    departamento,
    COUNT(*) AS empleados,
    ROUND(AVG(salario),2) AS salario_medio
FROM empleados
GROUP BY departamento
HAVING AVG(salario) > 45000
ORDER BY salario_medio DESC
"""

resultado = spark.sql(consulta)
resultado.show()

print("\n===== Plan de ejecución =====")

resultado.explain(True)
spark.stop()