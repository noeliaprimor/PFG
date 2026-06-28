#!/usr/bin/env python3
from pathlib import Path

from pyspark.sql import SparkSession


OUTPUT = Path("/workspace/output")

spark = (
    SparkSession.builder
    .appName("M3T2ValidateOutputs")
    .master("local[*]")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("WARN")

for name in ["tweets_valid", "tweets_quarantine", "tweets_metrics"]:
    path = OUTPUT / name
    print(f"\n== {name} ==")
    if not path.exists():
        print("No existe:", path)
        continue

    df = spark.read.parquet(str(path))
    print("Registros:", df.count())
    df.show(10, truncate=False)

spark.stop()
