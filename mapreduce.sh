#! /bin/bash

JAR_FILE = hadoop-streaming-2.5.jar

hadoop jar $HADOOP_HOME/${JAR_FILE} \
-file autoinc_mapper1.py -mapper autoinc_mapper1.py \
-file autoinc_reducer1.py -reducer autoinc_reducer1.py \
-input input/data.csv -output output/all_accidents

hadoop jar $HADOOP_HOME/${JAR_FILE} \
-file autoinc_mapper2.py -mapper autoinc_mapper2.py \
-file autoinc_reducer2.py -reducer autoinc_reducer2.py \
-input output/all_accidents -output output/make_year_count