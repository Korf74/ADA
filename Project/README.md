*To read the final notebook use this link :* http://nbviewer.jupyter.org/github/Korf74/ADA/blob/master/Project/Milestone3.ipynb

# Media coverage of violent events in war zone

## Abstract

Media is the first and often the only source of information in modern society and is supposed to ensure a certain integrity. The information medias provide, determines one global vision of the world. We aim to show here the loss of interest in the media for armed conflicts that tends to last over time and/or are located in developing countries. We believe that this practice suggests to the population that the situation has improved when it might have not. This study is based on violent events in a subset of countries that faced war during the last fifteen years, namely Afghanistan, Iraq, Mexico, Pakistan and Syria.

## Hypothesis

The media coverage of armed conflicts over time is not coherent with their importance and the press tends to lose interest for these conflicts even when they are still happening.

## Dataset

We use the "GDELT 2.0 Event Database" for the data. https://www.gdeltproject.org/data.html#rawdatafiles

The size of the data is huge (i.e 2.4 TB).  However, all the information we need is contained in this data.

We used as well the UCDP dataset.

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

`topArticle.sql` : the top countries which have the highest number of articles that are filter by EventCode

`topEvent.sql` : the top countries which have the highest number of events that are filter by EventCode.


* Run each of SQL command and download the file in CSV format.

With the CSV files you can run the notebook called `milestone2`

# Milestone 3

* The notebook is **Milestone3.ipynb**
* The report is **ADA_report.pdf**

For this milestone the division of work was as follows :

* Lucas : SQL Queries, Google BigQuery, interactive plots, notebook, correlations, analysis, final discussions 
* Niroshan : Folium maps, interactive plots, notebook, double scaled plots, analysis, final discussions
* Rémi : first version of the report from the notebook, report plots, notebook, first visualizations, data preprocessing, final discussions

For the final presentation, we will all work on the poster, and the talk will most likely be done by Niro and Lucas.




