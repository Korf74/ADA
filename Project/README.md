# Loss of interest in the media for armed conflits

## Abstract

Media is the first and often the unique source of information in the modern society, that is supposed  to ensure a certain integrity. The information they provide determine our global vision of the world. 
We aim to show the lost of interest in the media, for armed conflit, that tends to last over time. We believe that this practice suggests to the population that the situation has improved. 
For instance, over the last couple of years, we have been flooded by news about the Syrian conflit, whereas the situation in Afghanistan is overlooked, but it does not mean that the conflit is over.

Ideally, we also would like to show that the media coverage of armed conflit depends which countries are involved.


## Research questions

* The distribution of the number of article mentioned over the conflit duration.
* A space distribution of the number of articles/mentions based on the geolocation of a conflit.
* The correlation between countries involved in a conflit and the number of articles/mentions of it.


## Dataset
List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.

We will use the "GDELT 1.0 Event Database" for the data. https://www.gdeltproject.org/data.html#rawdatafiles

The data is provided as a downloadable file, the computer is not capable of store it. Therefore we will have to use clusters.

The size of the data is huge (i.e 2.4 TB), which is challenging.  However, we think that all the information we need is contained in this data. The documentation about each features is clear.

## A list of internal milestones up until project milestone 2
Milestone 2 deadline : 28 November 2017

* A stategy to extract the data.
* Create analyse functions that helps to build relevant data.
* Familiarize with the data.

## Questions for TAa

What is the best practice to deal with large amoungt of data ?
Do EPFL provide clusters to process the data ?

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


* Run each of SQL command and download the file.


_Note: The complete description of the data is contained in the notebook._



