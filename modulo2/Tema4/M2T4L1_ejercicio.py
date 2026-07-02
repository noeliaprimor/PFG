from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import time

spark = (
    SparkSession.builder
    .appName("EjercicioMonitorizacionSpark")
    .master("local[*]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

datos = [
    ("Matrix", "Accion", 136, 63),
    ("Titanic", "Drama", 194, 200),
    ("Avatar", "CienciaFiccion", 162, 237),
    ("Interstellar", "CienciaFiccion", 169, 165),
    ("Inception", "CienciaFiccion", 148, 160),
    ("Gladiator", "Accion", 155, 103),
    ("ElCaballeroOscuro", "Accion", 152, 185),
    ("PulpFiction", "Crimen", 154, 8),
    ("ForrestGump", "Drama", 142, 55),
    ("ElPadrino", "Crimen", 175, 6),
]

df = spark.createDataFrame(
    datos,
    ["pelicula", "genero", "duracion", "presupuesto"]
)

print("\nDatos originales")
df.show()

print("\nNúmero de películas por género")
resultado_genero = (
    df.groupBy("genero")
      .agg(
          F.count("*").alias("num_peliculas"),
          F.avg("duracion").alias("duracion_media"),
          F.avg("presupuesto").alias("presupuesto_medio")
      )
)

resultado_genero.show()

print("\nPelículas con presupuesto superior a 100 millones")
df.filter(F.col("presupuesto") > 100).show()

print("\nOrdenando películas por duración")
df.orderBy(F.desc("duracion")).show()

print("\nLa aplicación permanecerá activa 60 segundos.")
print("Abre Spark UI en: http://localhost:4040")

time.sleep(60)

spark.stop()
