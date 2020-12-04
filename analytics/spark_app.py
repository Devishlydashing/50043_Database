import os
import time

from pyspark import ml
from pyspark.ml.feature import CountVectorizerModel
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

def load_data(path):
    # df = spark.read.load(path, format="csv")
    df = spark.read.option("header", True).csv(path)
    return df

def sparse2dict(vec, idx2word):
    idxs = vec.indices
    vals = vec.values
    vals = vals.round(3)  
    return str({idx2word[i]:v for i,v in zip(idxs, vals)})

def tfidf_review_text(df):
    with Timer("TF-IDF for reviewText"):
        df = df.select(["reviewText"]).dropna()

    with Timer("TF-IDF pipeline"):
        tokenizer = ml.feature.Tokenizer(inputCol="reviewText", outputCol="token")
        cv = ml.feature.CountVectorizer(inputCol="token", outputCol="hash")
        idf = ml.feature.IDF(inputCol="hash", outputCol="tfidf")
        pipeline = ml.Pipeline(stages=[tokenizer, cv, idf])
        model = pipeline.fit(df)
        df = model.transform(df)

    stages = model.stages
    # print(f"stages: {stages}")

    vectorizers = [s for s in stages if isinstance(s, CountVectorizerModel)]
    vocab = [v.vocabulary for v in vectorizers]
    vocab = vocab[0]
    # print(vocab[-1])
    # print(f"Length of Vocab: {len(vocab[0])}")

    idx2word = {idx: word for idx, word in enumerate(vocab)}

    with Timer("Convert TF-IDF sparseVector to (word:value dict)"):
        my_udf_func = udf(lambda vector: sparse2dict(vector, idx2word), types.StringType())
        df = df.select("reviewText", my_udf_func("tfidf").alias("tfidf_final"))

    show_df(df, 10)
    return df

if __name__ == "__main__":
    
    with Timer("Spark script"):
        spark = SparkSession.builder.master("local[*]").getOrCreate()
        print("Running spark_app.py")

        df_reviews = load_data("kindle_reviews.csv") #specify path
        # df_reviews.show(5)
    
        df_tfidf = tfidf_review_text(df_reviews)