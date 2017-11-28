## How to get GDELT dataset ?


This section describes step by step methodology to get the necessary dataset for the project.

The chosen dataset is GDELT, which is one of the largest datasets among the others. It collects all the events such as conflict and news. 

We are interested in the armed conflict in following countries: Afghanistan, Iraq, Mexico, Pakistan and Syria. The period of interest is from 2000 to 2016.

In order to get the data we use the [Google Big Query](https://cloud.google.com/bigquery/?hl=en)
which contains the [GDELT full event records](https://www.gdeltproject.org/data.html#googlebigquery).

The methodology to extract the data.

* Connect to the Google Big Query which hold the GDELT data, click [here](https://bigquery.cloud.google.com/table/gdelt-bq:full.events)

There you will find a space to write a SQL query to the dataset. Several SQL queries are made. The following section describe the purpose of the SQL files.



`mainExtraction.sql` : returns a table which count the number article and the number of event per month, country and EventCode.

`topArticle.sql` : the top 40 countries which have the highest number of articles that are filter by EventCode

`topEvent.sql` : the top 40 countries which have the highest number of events that are filter by EventCode.


* Run each of SQL command and download the file.


_Note: The complete description of the data is contained in the notebook._



