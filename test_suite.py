import unittest
from test_self_drive_car import SelfDrivingCarTest
from test_sensor import SensorTest

class SuiteTest(object):
    def __init__(self):
        pass
    @classmethod
    def suite(cls):
        suite = unittest.TestSuite()
        suite.addTest(SelfDrivingCarTest('test_stop'))
        suite.addTest(SensorTest('test_detect'))
        return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(SuiteTest.suite())

