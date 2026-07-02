from pyspark.sql import SparkSession

from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline

spark = (
    SparkSession.builder
    .appName("MLlibPeliculas")
    .master("local[*]")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("peliculas_mllib.csv")
)

print("\nDatos originales")
df.show()

indexer = StringIndexer(
    inputCol="genero",
    outputCol="genero_index"
)

assembler = VectorAssembler(
    inputCols=[
        "duracion",
        "presupuesto",
        "genero_index"
    ],
    outputCol="features"
)

lr = LogisticRegression(
    featuresCol="features",
    labelCol="label",
    maxIter=10
)

pipeline = Pipeline(
    stages=[
        indexer,
        assembler,
        lr
    ]
)

modelo = pipeline.fit(df)

predicciones = modelo.transform(df)

print("\nPredicciones")
predicciones.select(
    "pelicula",
    "genero",
    "label",
    "prediction",
    "probability"
).show(truncate=False)

spark.stop()