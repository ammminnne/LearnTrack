from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, desc

spark = SparkSession.builder \
    .appName("LearnTrack Analytics") \
    .config("spark.mongodb.input.uri", "mongodb://mongos-router:27017/learntrack.activity_logs") \
    .config("spark.mongodb.output.uri", "mongodb://mongos-router:27017/learntrack.course_stats") \
    .getOrCreate()

print("[-] Spark Session Started. Reading data...")

# Read Data
df = spark.read.format("mongo").load()

# Process Data
popular_courses = df.groupBy("course_id") \
    .agg(count("*").alias("total_interactions")) \
    .orderBy(desc("total_interactions"))

# WRITING TO PORT 8020
hdfs_path = "hdfs://namenode:8020/output/popular_courses"
print("[-] Attempting to write to HDFS at: " + hdfs_path)

popular_courses.write.csv(hdfs_path, mode="overwrite", header=True)

print("[-] SUCCESS: Results saved to HDFS.")
spark.stop()