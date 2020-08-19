# -*- coding: utf-8 -*-
import unittest
import logging
import warnings

from pyspark.sql import SparkSession


class PysparkTestCase(unittest.TestCase):

  @classmethod
  def suppress_py4j_logging(cls):
    warnings.filterwarnings(
      action="ignore",
      message="unclosed",
      category=ResourceWarning)
    logger = logging.getLogger("py4j")
    logger.setLevel(logging.ERROR)

  @classmethod
  def setUpClass(cls):
    cls.suppress_py4j_logging()
    cls.spark = SparkSession.builder.master('local').getOrCreate()
    cls.spark.sparkContext.setLogLevel('WARN')

  @classmethod
  def tearDownClass(cls):
    cls.spark.stop()

  @classmethod
  def is_dataframe_equal(cls, df1, df2):
    if not df1.schema.simpleString() == df2.schema.simpleString():
      print(df1.schema.simpleString())
      print(df2.schema.simpleString())
      return False

    if df1.join(df2, df1.columns, "left_anti").count() > 0:
      return False
    return True


if __name__ == '__main__':
  unittest.main()