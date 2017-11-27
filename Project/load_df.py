from pyspark import SparkContext
from pyspark.sql import SQLContext, DataFrameReader


# convert a text line to words vector



if __name__ == '__main__':

    sc = SparkContext()
    sqlContext = SQLContext(sc)



    hdfs_pathname = "/datasets/GDELT.MASTERREDUCEDV2.1979-2013/GDELT.MASTERREDUCEDV2.TXT"

    text_file = sc.textFile(hdfs_pathname)
    n = 10
    header = text_file.first()

    text_file = text_file.filter(lambda line : line != header) # pas optimal
    #df = spark.read().csv(hdfs_pathname,sep ="\t")
    #df.printSchema()
    #df.printSchema()

    rdd_list = text_file.map(lambda line : line.split("\t"))
    rdd_list = rdd_list.filter(lambda l:  len(l) == 17)

    df = rdd_list.toDF(header.split("\t"))



    take_n = rdd_list.take(n)
    output_path ="/home/vijayara/niro.csv"

    df.registerAsTable('df_table')
    sql_request= "SELECT Date,Source,Target,CAMEOCode,NumEvents,NumArts " \
          "FROM df_table " \
          "WHERE (Source IN ('AFG','SYR','IRQ','MEX', 'PAK') OR Target IN ('AFG','SYR','IRQ','MEX', 'PAK')) AND " \
          "(CAMEOCode LIKE '18%' OR CAMEOCode LIKE '19%' OR CAMEOCode LIKE '20%' )" \

    sql_request_group_by = "SELECT MonthYear,Target,EventCode,SUM(NumEvents), SUM(NumArts) " \
                  "FROM df_table " \
                  "WHERE (Target IN ('AFG','SYR','IRQ','MEX', 'PAK')) AND " \
                  "(CAMEOCode LIKE '18%' OR CAMEOCode LIKE '19%' OR CAMEOCode LIKE '20%' ) AND " \
                           "(Date > 20021231 AND Date < 20140101) " \
                           "GROUP BY ( SUBSTRING( Date ,1 , 6) AS MonthYear ,Target, SUBSTRING(CAMEOCode,1,2) AS EventCode )" \



    df_filter = sqlContext.sql(sql_request_group_by)
    df_filter.show()
    #print(df_filter.count())
    #df_filter.coalesce(1).write.json(output_path)


    sc.stop()