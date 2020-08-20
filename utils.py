import numpy as np
import pyspark.sql.functions as F
import pyspark.sql.types as T


def cosine_similarity(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


cosine_similarity_udf = F.udf(cosine_similarity, T.FloatType())


def compute_similarity(df):
    rst = df.withColumn("c", cosine_similarity_udf(F.col("a"), F.col("b"))).select("c")
    return rst
