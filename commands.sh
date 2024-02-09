rm -rf ./output_wordcount
spark-submit ./wordcount.py ./wiki.txt ./output_wordcount


rm -rf ./output_bigram
spark-submit ./bigram.py ./wiki.txt ./output_bigram