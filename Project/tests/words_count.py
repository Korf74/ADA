import json
import re
from pyspark.sql import *
from pyspark import SparkContext, SQLContext

# context initialization
sc = SparkContext()
sqlContext = SQLContext(sc)

# read the input file line by line
text_file = sc.textFile("/datasets/GDELT.MASTERREDUCEDV2.1979-2013/GDELT.MASTERREDUCEDV2.TXT")

counts_rdd = text_file
