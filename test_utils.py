from BaseTest import PysparkTestCase
import utils

import pyspark.sql.types as T
import pyspark.sql.functions as F

import pandas as pd


print("test utils")

class UtilsTest(PysparkTestCase):
    def test_compute_similarity(self):
        arrays = [
            ([1, 2], [2, 4], 1.0),
            ([1, 1], [-1, -1], -1.0),
            ([1, 2], [2, 1], 0.8)
        ]

        schema = T.StructType([
            T.StructField('a', T.ArrayType(T.IntegerType()), nullable=False),
            T.StructField('b', T.ArrayType(T.IntegerType()), nullable=False),
            T.StructField('c', T.FloatType(), nullable=False)
        ])

        df = self.spark.createDataFrame(
            pd.DataFrame(
                arrays
            ),
            schema
        )
        df_expect = df.select(F.col('c'))

        df_test = utils.compute_similarity(df)

        self.assertTrue(
            self.is_dataframe_equal(
                df_test,
                df_expect
            )
        )