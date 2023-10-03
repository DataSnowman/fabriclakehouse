import sys
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("MyApp").getOrCreate()
    spark.sparkContext.setLogLevel("DEBUG")

    tableName = "streamingtable2"
    deltaTablePath = "Tables/" + tableName

    df = spark.readStream.format("rate").option("rowsPerSecond", 1).load()

    query = df.writeStream.outputMode("append").format("delta").option("path", deltaTablePath).option("checkpointLocation", deltaTablePath + "/checkpoint").start()