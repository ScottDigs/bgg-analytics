from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("spark://localhost:7077") \
    .appName("LocalSparkIceberg") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.executor.memory", "4g") \
    .config("spark.executor.cores", "2") \
    .config("spark.network.timeout", "300s") \
    .config("spark.scheduler.maxRegisteredResourcesWaitingTime", "600s") \
    .config("spark.hadoop.fs.s3a.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.secret.key", "password") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://localhost:9000") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .getOrCreate()


# Sample DataFrame creation
data = [("James", "Smith"), ("Anna", "Rose"), ("Robert", "Williams")]
columns = ["First Name", "Last Name"]

df = spark.createDataFrame(data, columns)

# Show DataFrame content
df.show()

# Stop the session when done
spark.stop()
