import sys
from pyspark import SparkContext, SparkConf
from operator import add
def generate_bigrams(line):
    # Convert to lower case and remove non-alphabetic characters
    words = [word for word in line.lower().split() if word.isalpha()]
    # Generate bigrams
    return [((words[i], words[i + 1]), 1) for i in range(len(words) - 1)]

# Initialize Spark context
conf = SparkConf().setAppName("BigramCount")
sc = SparkContext(conf=conf)

# Read data from text file
lines = sc.textFile(sys.argv[1])

# Generate bigrams from each line and flatten the list
bigrams = lines.flatMap(generate_bigrams)

# Count the occurrence of each bigram
bigramCounts = bigrams.reduceByKey(lambda a, b: a + b).map(lambda x: (x[0][0], (x[0][1], x[1])))

firstWordsCount = bigrams.map(lambda bigram: (bigram[0][0], 1)).reduceByKey(lambda a, b: a + b)

joined = firstWordsCount.join(bigramCounts)

bigramFreq = joined.map(lambda x: ((x[0], x[1][1][0]), x[1][1][1] / x[1][0]))

# Save the result to a text file
bigramFreq.coalesce(1, shuffle=True).saveAsTextFile(sys.argv[2] + "_freq")
bigramCounts.coalesce(1, shuffle=True).saveAsTextFile(sys.argv[2] + "_count")

sc.stop()

