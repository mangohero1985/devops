import numpy as np
import pyspark.sql.functions as F
import pyspark.sql.types as T


@udf(T.FloatType())
def cosine_similarity(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def compute_similarity(df):
    rst = df \
        .withColumn("cos_sim", cosine_similarity(F.col("a"), F.col("b"))) \
        .select("cos_sim")
    return rst
