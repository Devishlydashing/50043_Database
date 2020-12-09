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
        print("\nStart timer:", self.name)
        
    def __exit__(self, type, value, traceback):
        duration = time.time() - self.start
        duration = round(duration, self.decimals)
        print("Ended timer: {}: {} s".format(self.name, duration))

def show_df(df, no_rows_to_show):
    rows = df.take(no_rows_to_show)
    for r in rows:
        print(r)

def load_data(path):
    file_type = (Path(path).suffix)
    if file_type == ".csv":
        df_reviews = spark.read.option("header", True).csv(path)
        return df_reviews

    elif file_type == ".json":
        df_meta = spark.read.json(path)
        return df_meta


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

    rdd_price_reviewText = df.rdd
    rdd_price_reviewLength = rdd_price_reviewText.mapValues(get_review_length)

    with Timer("Map reduce pearson correlation"):
        pearson_value = map_reduce_pearson(rdd_price_reviewLength)

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
        df.unpersist()
        # df.cache()

    stages = model.stages
    # print(f"stages: {stages}")

    vectorizers = [s for s in stages if isinstance(s, CountVectorizerModel)]
    vocab = [v.vocabulary for v in vectorizers]
    vocab = vocab[0]
    # print(f"Length of Vocab: {len(vocab[0])}")

    idx2word = {idx: word for idx, word in enumerate(vocab)}

    with Timer("Convert TF-IDF sparseVector to (word:value dict)"):
        my_udf_func = udf(lambda vector: sparse2dict(vector, idx2word), types.StringType())
        df = df.select("reviewText", my_udf_func("tfidf").alias("tfidf"))
    return df

def export_pearson_results(pearson_value):
    with Timer("Exporting Pearson results to HDFS"):
        with open("pearson_results.txt", "w") as f:
            f.write("Pearson Correlation between Price & Average Review Length: " + str(pearson_value))
    return

def export_tfidf_results(df):
    with Timer("Exporting tfidf results to HDFS"):
        df.write.format('csv').option('header',True).mode('overwrite').option('sep','|').save('output/')
    return

if __name__ == "__main__":

    with Timer("Spark script"):
        print("Running spark_app.py")
        
        # Production
        with Timer("Retrieve IP address from ip.txt file sent from master ec2"):
            with open('/home/hadoop/ip.txt', 'r') as f: 
                mongo_ip = f.readlines()
                mongo_ip = mongo_ip[2].split("=")[1].rstrip('\r\n')
                mongo_ip = mongo_ip.strip()

        mongo_db_address = "mongodb://{}/meta.newmetadata".format(mongo_ip)
        spark = SparkSession.builder.master("local[*]").config("spark.mongodb.input.uri", mongo_db_address).config("spark.mongodb.output.uri", mongo_db_address).getOrCreate()
        df_reviews = load_data("/user/hadoop/reviews/reviews.csv")
        df_meta = spark.read.format("mongo").load()

        # Local =====
        # spark = SparkSession.builder.master("local[*]").getOrCreate()
        # df_reviews = load_data("./data/reviews.csv")
        # df_meta = load_data("./data/mongo_data.json")
        # ======

        pearson_value = pearson_price_vs_review_length(df_meta, df_reviews)
        df_tfidf = tfidf_review_text(df_reviews)

        # Present results
        print(f"Correlation value:{pearson_value}\n")

        show_df(df_tfidf,10)
        df_tfidf.show()

        export_pearson_results(pearson_value)
        export_tfidf_results(df_tfidf)
