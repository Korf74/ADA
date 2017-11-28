## How to get GDELT dataset from the cluster ?

This section describes step by step methodology to get the necessary dataset for the project. The chosen dataset is GDELT, which is one of the largest datasets among the others. It collects all the events such as conflict and news. A subset of this dataset is present in the cluster of the EPFL. The address of the cluster is « iccluster060.iccluster.epfl.ch » .  After the configuration of the spark service and yarn service in the localhost as specified in the following link  «https://github.com/epfl-ada/ADA2017-Tutorials/tree/master/05%20-%20Using%20the%20cluster »  we are able to send jobs to the cluster that host spark services. 

In order to get the data in the local file, you need to create a python2.7 environment using the Anaconda navigator. 

Activate the environment using 

```
 source activate <name_environment>
```

Then, Run the spark job called load_df.py using

```
<spark_directory>/bin/spark-submit --master yarn load_df.py
```

After the job is completed, all the partition of the of dataframe is present in the HDFS file called « niroSource » . This step is to merge the partition and move to a local file. 

```
hadoop fs -getmerge niroSource   <local_file>.txt
```

Now the file is merged and reside in the cluster . To copy this file into the local machine, scp command is used.

```
scp  <GASPARD>@iccluster060.iccluster.epfl.ch:/<local_file>.txt  <local_machine_Path>
```

Now you have the text  file into the local machine. 

We exploit this text file in the following notebook :  .. 

Look the notebook to know what we do with the data.