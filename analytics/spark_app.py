import os
import time

from pyspark import ml
from pyspark.sql import SparkSession, utils
from pyspark.sql.functions import udf
from pyspark.sql import types

def show_df(df, n_show):
    rows = df.take(n_show)
    for r in rows:
        print(r)

def tfidf_review_text(df):
    df = df.select(["reviewText"]).dropna()

    tokenizer = ml.feature.Tokenizer(inputCol="reviewText", outputCol="token")
    hasher = ml.feature.CountVectorizer(inputCol="token", outputCol="hash")
    idf = ml.feature.IDF(inputCol="hash", outputCol="tfidf")
    pipeline = ml.Pipeline(stages=[tokenizer, hasher, idf])
    pipeline = pipeline.fit(df)
    df = pipeline.transform(df)
    
    return df