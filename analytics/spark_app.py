import os
import time
from operator import add
from pathlib import Path

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
    file_type = (Path(path).suffix)
    if file_type == ".csv":
        df_reviews = spark.read.option("header", True).csv(path)
        return df_reviews

    elif file_type == ".json":
        df_meta = spark.read.json(path)
        return df_meta

def export_results():
    # with Timer("Exporting results analytics results to HDFS"):
        # df
    return

def tokenize(text):
    return text.strip().lower().split()


def get_review_length(text):
    return len(tokenize(text))

def map_fn_pearson(pair):
    x, y = pair
    return [
        ("n", 1),
        ("xy", x * y),
        ("x", x),
        ("y", y),
        ("x_square", x ** 2),
        ("y_square", y ** 2)
    ]

def apply_pearson_formula(result_list):
    sums = {key: value for key, value in result_list}
    assert set(sums.keys()) == {"n", "xy", "x", "y", "x_square", "y_square"}

    top = (sums["n"] * sums["xy"]) - (sums["x"] * sums["y"])
    bottom_left = ((sums["n"] * sums["x_square"]) - sums["x"] ** 2) ** 0.5
    bottom_right = ((sums["n"] * sums["y_square"]) - sums["y"] ** 2) ** 0.5
    return top / (bottom_left * bottom_right)

def map_reduce_pearson(rdd):
    rdd = rdd.flatMap(map_fn_pearson)
    rdd = rdd.reduceByKey(add)
    return apply_pearson_formula(rdd.collect())

def pearson_price_vs_review_length(df_meta, df_reviews):
    df_meta = df_meta.select(["asin", "price"])
    df_reviews = df_reviews.select(["asin", "reviewText"])
    df = df_meta.join(df_reviews, on="asin", how="inner")
    df = df.drop("asin")
    df = df.dropna()

    df.show()

    rdd_price_reviewText = df.rdd
    rdd_price_reviewLength = rdd_price_reviewText.mapValues(get_review_length)

    with Timer("Map reduce pearson correlation"):
        pearson_value = map_reduce_pearson(rdd_price_reviewLength)

    print("Correlation value:", pearson_value)

    with open("results_pearson.txt", "w") as f:
        f.write("Pearson Correlation between Price & Average Review Length: " + str(pearson_value))

    return pearson_value

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

        df_reviews = load_data("./output/mysql_reviews_data.csv")
        df_meta = load_data("./output/mongo_data.json")
        
        df_reviews.show(5)
        df_meta.show(5)

        pearson_value = pearson_price_vs_review_length(df_meta, df_reviews)
        df_tfidf = tfidf_review_text(df_reviews)