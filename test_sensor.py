import unittest
from sensor import Sensor
from person import Person
from vehicle import Vehicle

class SensorTest(unittest.TestCase):
    def setUp(self):
        self.sensor = Sensor()
        self.speed = 0

    def test_detect(self):
        self.speed = 25
        self.assertIsInstance(self.sensor.detect(self.speed), Vehicle)
