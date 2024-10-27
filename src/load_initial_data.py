import os
import re

from pyspark.sql.functions import input_file_name, col

from src.spark_conn import get_spark

def load_bgg_files_to_delta():
    
    spark = get_spark()
    tables = ["game_info", "games", "reviews"]

    for table in tables:
        ingest_path = os.path.join(".data", "ingest", table)
        output_path = os.path.join(".data", "spark", table)
        df = spark.read.format("csv").option("header", "true").load(f"{ingest_path}/*.csv")

        df = df.withColumn("source_file", input_file_name())
        df = df.select(*[col(c).alias(re.sub("\W+", "", c).lower()) for c in df.columns])
        df.write.format("delta").mode("overwrite").save(output_path)

        print(f"Table {table} loaded\n Record count: {df.count()}")
    spark.stop()

if __name__ == "__main__":
    load_bgg_files_to_delta()
