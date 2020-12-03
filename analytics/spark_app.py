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
