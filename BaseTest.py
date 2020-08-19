# -*- coding: utf-8 -*-
import unittest
import logging
import warnings
import glob

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
    cls.spark = SparkSession.builder.master('local[2]').getOrCreate()
    cls.spark.sparkContext.setLogLevel('WARN')
    for file in glob.glob('/home/jovyan/tests/*.py'):
      cls.spark.sparkContext.addPyFile(file)
    # cls.spark.sparkContext.addPyFile('/home/jovyan/tests/test_utils.py')
    # cls.spark.sparkContext.addPyFile('/home/jovyan/tests/utils.py')


  @classmethod
  def tearDownClass(cls):
    cls.spark.stop()
    print("pyspark unittest finished")

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