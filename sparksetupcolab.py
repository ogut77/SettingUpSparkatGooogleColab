!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!wget -q http://ftp.itu.edu.tr/Mirror/Apache/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz
!tar xf spark-2.4.0-bin-hadoop2.7.tgz
!pip install -q findspark

import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-2.4.0-bin-hadoop2.7"

import findspark
findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()

!ls

from pyspark import SparkContext
sc = SparkContext.getOrCreate()
#show first 5 lines
lines = sc.textFile("sample_data") 
lines.take(5)



#number of lines
print(lines.count())
