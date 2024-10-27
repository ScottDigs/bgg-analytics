
from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip

def get_spark() -> SparkSession:
    builder = SparkSession.builder.appName("DeltaLakeExample") \
        .master("local[*]") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .config("spark.driver.host","127.0.0.1") \
        .config("spark.driver.bindAddress","127.0.0.1")

    spark = configure_spark_with_delta_pip(builder).getOrCreate()
    return spark