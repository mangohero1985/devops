import numpy as np
import pyspark.sql.functions as F
import pyspark.sql.types as T
from pyspark.sql.functions import udf

@udf(T.FloatType())
def cosine_similarity(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def compute_similarity(df):
    rst = df.withColumn("c", cosine_similarity(F.col("a"), F.col("b"))).select("c")
    return rst

