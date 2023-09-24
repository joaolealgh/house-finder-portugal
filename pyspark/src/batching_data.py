import logging

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,FloatType,IntegerType,StringType
from pyspark.sql.functions import from_json,col

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')

logger = logging.getLogger("spark_structured_streaming")

def create_spark_session():
    """
    Creates the Spark Session with suitable configs.
    """
    try:
        # Spark session is established with postgres and kafka jars. Suitable versions can be found in Maven repository.
        spark = SparkSession \
                .builder \
                .appName("SparkStructuredStreaming") \
                .config("spark.jars.packages", "spark/jars/postgresql-42.6.0.jar,spark/jars/spark-sql-kafka-0-10_2.12-3.3.0.jar") \
                .getOrCreate()
        spark.sparkContext.setLogLevel("ERROR")
        logging.info('Spark session created successfully')
    except Exception:
        logging.error("Couldn't create the spark session")

    return spark

def create_initial_dataframe(spark_session):
    """
    Reads the streaming data and creates the initial dataframe accordingly.
    """
    try:
        # Gets the streaming data from topic supercasa_houses
        df = spark_session \
              .read \
              .format("kafka") \
              .option("kafka.bootstrap.servers", "localhost:9092") \
              .option("subscribe", "supercasa_houses") \
              .option("startingOffsets", "earliest") \
              .load()
        logging.info("Initial dataframe created successfully")
    except Exception as e:
        logging.warning(f"Initial dataframe couldn't be created due to exception: {e}")

    return df

def create_final_dataframe(df, spark_session):
    """
    Modifies the initial dataframe, and creates the final dataframe.
    """
    schema = StructType([
                StructField("Link",StringType(),False),
                StructField("Title",StringType(),False),
                StructField("Price",StringType(),False),
                StructField("Location",StringType(),False),
                StructField("Features",StringType(),False),
                StructField("Highlights",StringType(),False),
                StructField("Description text",StringType(),False)
            ])

    df = df.selectExpr("CAST(value AS STRING)").select(from_json(col("value"),schema).alias("data")).select("data.*")
    print(df)
    return df

def start_streaming(df):
    """
    Starts the streaming to table spark_streaming.supercasa_house in postgres
    """
    logging.info("Streaming is being started...")
    my_query = (df.write
                  .format("jdbc")
                  .option("url", "jdbc:postgresql://localhost:5432/web_scraping_db")
                  .option("driver", "org.postgresql.Driver")
                  .option("dbtable", "supercasa_house")
                  .option("user","postgres")
                  .option("password","password"))

    return my_query


def write_streaming_data():
    spark = create_spark_session()
    df = create_initial_dataframe(spark)
    df_final = create_final_dataframe(df, spark)
    start_streaming(df_final)


if __name__ == '__main__':
    write_streaming_data()
