from pyspark.sql import SparkSession
from pyspark.sql.functions import input_file_name
from delta import configure_spark_with_delta_pip

builder = SparkSession.builder.appName("DeltaLakeExample") \
    .master("local[*]") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .config("spark.driver.host","127.0.0.1") \
    .config("spark.driver.bindAddress","127.0.0.1") \

spark = configure_spark_with_delta_pip(builder).getOrCreate()

# Example Delta Lake operations
data = [(1, "foo"), (2, "bar"), (3, "baz")]
columns = ["id", "value"]

# df = spark.createDataFrame(data, columns)

# df.show()

# df.write.format("delta").save("/tmp/spark/delta-table")

df = spark.read.format("csv").option("header", "true").load(".data/ingest/games/*.csv")

df = df.withColumn("source_file", input_file_name())
df.show(10)