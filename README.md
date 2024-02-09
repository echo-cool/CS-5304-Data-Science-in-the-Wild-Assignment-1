# CS 5304 Data Science in the Wild - Assignment 1

## Setup

### Install Spark

```bash
pip install pyspark
```
Download and install Spark 3.0 on your machine: 
https://dlcdn.apache.org/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz
Unpack the compressed TAR ball, either by using the following command, or double-click on the package.
```bash
tar xvf spark-3.5.0-bin-hadoop3.tgz
```

### Download data file

Download the data file from the following link and place it in the root directory of the project.

```bash
https://drive.google.com/file/d/1FgByt-JMfrZ3g-WdrzZeXXyMARCjJPXa/view
```

## Run the code

### Wordcount
```bash
rm -rf ./output_wordcount
spark-submit ./wordcount.py ./wiki.txt ./output_wordcount
```

### bigram

```bash
rm -rf ./output_bigram
spark-submit ./bigram.py ./wiki.txt ./output_bigram
```

## Output

* The output of the wordcount and bigram will be stored in the output_wordcount and output_bigram directories respectively.