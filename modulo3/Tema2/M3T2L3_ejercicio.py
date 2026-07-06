from pyspark.sql import functions as F
from pyspark.sql import SparkSession
spark = (SparkSession.builder
         .appName("SinksYConectores")
         .master("local[*]")
         .getOrCreate())

datos = [
    ("pedido-1", "cli-1", 25.5, "EUR", "web"),
    ("pedido-2", "cli-2", 40.0, "EUR", "app"),
    ("pedido-3", "cli-1", 15.0, "EUR", "web"),
    ("pedido-4", "cli-3", 80.0, "EUR", "tienda")
]

columnas = ["pedido_id", "cliente_id", "importe", "moneda", "canal"]
df = spark.createDataFrame(datos, columnas)
pedidos_procesados = (
    df
    .withColumn(
        "categoria_importe",
        F.when(F.col("importe") >= 50, "alto")
         .otherwise("normal")
    )

    .withColumn("fecha_proceso", F.current_date())
)

print("Salida por consola:")

pedidos_procesados.show(truncate=False)

ruta_salida = "output/pedidos_parquet"

(pedidos_procesados.write
 .format("parquet")
 .mode("overwrite")
 .partitionBy("canal")
 .save(ruta_salida))

print(f"Datos guardados en: {ruta_salida}")

spark.stop()
