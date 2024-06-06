from pyspark.sql import SparkSession
import happybase

def process_data():
    # Initialize Spark Session
    spark = SparkSession.builder \
        .appName("DistributedDataProcessing") \
        .getOrCreate()

    # Sample data processing with Spark SQL
    data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
    df = spark.createDataFrame(data, ["Name", "Value"])
    df.createOrReplaceTempView("people")
    result = spark.sql("SELECT Name, Value FROM people WHERE Value > 1")
    result.show()

    # Stop Spark session
    spark.stop()

if __name__ == "__main__":
    process_data()

