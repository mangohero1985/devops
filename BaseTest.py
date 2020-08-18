# -*- coding: utf-8 -*-
import logging
import unittest
import warnings


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

    @classmethod
    def is_dataframe_equal(cls, df1, df2):
        if not df1.schema.simpleString() == df2.schema.simpleString():
            return False

        if df1.join(df2, df1.columns, "left_anti").count() > 0:
            return False
        return True


if __name__ == '__main__':
    unittest.main()
