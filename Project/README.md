# Loss of interest in the media for armed conflits

## Abstract

Media is the first and often the unique source of information in the modern society, that is supposed  to ensure a certain integrity. The information they provide determine our global vision of the world. 
We aim to show the lost of interest in the media, for armed conflit, that tends to last over time. We believe that this practice suggests to the population that the situation has improved. 
This study is based of the violent events in a subset of countries that faced war during the last fifteen years. Afghanistan, Iraq, Mexico, Pakistan and Syria were choosen.


## Research questions

* The distribution of the number of article mentioned over the conflit duration.
* A space distribution of the number of articles/mentions based on the geolocation of a conflit.
* The correlation between countries involved in a conflit and the number of articles/mentions of it.



## Dataset

We will use the "GDELT 2.0 Event Database" for the data. https://www.gdeltproject.org/data.html#rawdatafiles

The size of the data is huge (i.e 2.4 TB).  However, all the information we need is contained in this data. 

## How to get GDELT dataset ?


This section describes step by step methodology to get the necessary dataset for the project.

The chosen dataset is GDELT, which is one of the largest datasets among the others. It collects all the events such as conflict and news. 

We are interested in the armed conflict in following countries: Afghanistan, Iraq, Mexico, Pakistan and Syria. The period of interest is from 2000 to 2016.

In order to get the data we use the [Google Big Query](https://cloud.google.com/bigquery/?hl=en)
which contains the [GDELT full event records](https://www.gdeltproject.org/data.html#googlebigquery).

The methodology to extract the data.

* Connect to the Google Big Query which hold the GDELT data, click [here](https://bigquery.cloud.google.com/table/gdelt-bq:full.events)

There you will find a space to write a SQL query to the dataset. Several SQL queries are made and the following section describe the purpose of the SQL files.



`mainExtraction.sql` : returns a table which count the number article and the number of event per month, country and EventCode.

`topArticle.sql` : the top 40 countries which have the highest number of articles that are filter by EventCode

`topEvent.sql` : the top 40 countries which have the highest number of events that are filter by EventCode.


* Run each of SQL command and download the file in CSV format.

With the CSV files you can run the notebook called `milestone2`




