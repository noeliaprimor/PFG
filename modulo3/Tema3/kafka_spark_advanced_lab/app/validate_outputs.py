#!/usr/bin/env python3
from pathlib import Path

from pyspark.sql import SparkSession


OUTPUT = Path("/workspace/output")
TABLES = [
    "silver_orders",
    "quarantine_orders",
    "merchant_metrics",
    "alerts",
]


spark = (
    SparkSession.builder
    .appName("M3T3AdvancedValidateOutputs")
    .master("local[*]")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("WARN")

for table in TABLES:
    path = OUTPUT / table
    print(f"\n== {table} ==")
    if not path.exists():
        print("No existe:", path)
        continue

    df = spark.read.parquet(str(path))
    print("Registros:", df.count())
    df.printSchema()
    df.show(10, truncate=False)

spark.stop()
