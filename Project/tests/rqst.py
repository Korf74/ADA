import json
from pyspark.sql import *
from pyspark import SparkContext, SQLContext

# context initialization
sc = SparkContext()
sqlContext = SQLContext(sc)

df = sqlContext.read.format('csv').options(header='true', inferSchema='true').load('FILE.csv')


