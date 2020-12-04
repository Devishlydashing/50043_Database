import os
import time

from pyspark import ml
from pyspark.sql import SparkSession, utils
from pyspark.sql.functions import udf
from pyspark.sql import types

class Timer(object):
    def __init__(self, name, decimals=1):
        self.name = name
        self.decimals = decimals

    def __enter__(self):
        self.start = time.time()
        print("Start timer:", self.name)
        
    def __exit__(self, type, value, traceback):
        duration = time.time() - self.start
        duration = round(duration, self.decimals)
        print("Ended timer: {}: {} s".format(self.name, duration))

def show_df(df, no_rows_to_show):
    rows = df.take(no_rows_to_show)
    for r in rows:
        print(r)

def tfidf_review_text(df):
    with Timer("TF-IDF for reviewText"):
        df = df.select(["reviewText"]).dropna()

    with Timer("TF-IDF pipeline"):
        tokenizer = ml.feature.Tokenizer(inputCol="reviewText", outputCol="token")
        hasher = ml.feature.CountVectorizer(inputCol="token", outputCol="hash")
        idf = ml.feature.IDF(inputCol="hash", outputCol="tfidf")
        pipeline = ml.Pipeline(stages=[tokenizer, hasher, idf])
        model = pipeline.fit(df)
        df = model.transform(df)

    return df

if __name__ == "__main__":
    
    with Timer("My spark script"):
        print("Running spark_app.py")
