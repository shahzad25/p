from pyspark.sql import *
from pyspark import SparkConf
from lib.logger import Log4j
from lib.utils import get_spark_app_config

# cluster manager is defined as a master with local multi threaded JVM with three threads.
# SparkSession is a spark driver
#if __name__ == "__main__":
#    spark = SparkSession.builder \
#        .appName("Hello Spark") \
#        .master("local[3]") \
#        .getOrCreate()

if __name__ == "__main__":
    conf = get_spark_app_config()
    spark = SparkSession.builder \
            .config(conf=conf) \
            .getOrCreate()

    logger = Log4j(spark)

    logger.info("Starting HelloSpark")
    # Your processing code
    conf_out = spark.sparkContext.getConf()
    logger.info(conf_out.toDebugString())

    logger.info("Finisehd HelloSpark")
    spark.stop()
