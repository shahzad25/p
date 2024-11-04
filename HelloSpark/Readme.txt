I set up using PyCharm.

1. Create new project
2. Custom enviorment -> Type -> Virtualenv
3. Base Python is: C:\Users\shahz\AppData\Local\Programs\Python\Python312\python.exe
4. Location: C:\Labs\Udemy\ApacheSpark3Beginner\HelloSpark\pythonProject\.venv

Then once project is done. Open Settings -> and install pyspark (3.5.1) and pytest (any version)
spark home is at: C:\demo\spark-3.5.1
spark conf is at: C:\demo\spark-3.5.1\conf
update spark-defaults.conf by adding below line:
spark.driver.extraJavaOptions	   -Dlog4j.configuration=file:log4j.properties -Dspark.yarn.app.container.log.dir=app-logs -Dlogfile=hello-spark

Q/A
-> Which configuration is used to pass values to Spark driver JVM -> spark.driver.extraJavaOptions
-> You can inform spark that log4j.properties file is present in the current directory using the following configuration -> -Dlog4j.configuration=file:log4j.properties
-> What is the use of spark.yarn.app.container.log.dir variable? -> This variable used by YARN log aggregator to find your application log files/log4j file appened will create log files in this directory.
-> You can define spark.driver.extraJavaOptions in the following file -> SPARK_HOME/conf/spark-defaults.conf
-> Following Spark application configuration precedence is correct
enviroment variable -> spark-defaults.conf -> spark-submit command line -? SparkConf
-- Here is how spark-submit works.
spark-submit --master local[3] --conf "spark.app.name=Hello Spark" --conf spark.eventlog.enabled=false HelloSpark.py
--> SparkConf() object is where we use appName and master.





SparkContext is a class that represents a connection to a Spark cluster and is the primary entry point to Spark functionality.
Can be used to get SparkConf object. was an entry point to Programming Spark in older version.
A SparkContext represents the connection to a Spark cluster, and can be used to create RDDs, accumulators and broadcast variables on that cluster.
Only one SparkContext should be active per JVM


