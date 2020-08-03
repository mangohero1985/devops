import unittest
from unittest import TestCase
from SelfDrivingCar import SelfDrivingCar

class SelfDrivingCarTest(TestCase):
    
    @classmethod
    def setUpClass(cls):
      print('called once before any tests in class')

    @classmethod
    def tearDownClass(cls):
      print('\ncalled once after all tests in class')
    
    def setUp(self):
        # Fixture
        self.car = SelfDrivingCar()
        self.car.speed = 5
 
    def test_stop(self):
 
        self.car.stop()
        self.assertEqual(0, self.car.speed)
    def test_accelerate(self):
        
        self.car.accelerate()
        self.assertEqual(6, self.car.speed)
    
    def test_decelerate(self):
        
        self.car.decelerate()
        self.assertEqual(4, self.car.speed)

    def tearDown(self):
        
        del self.car

if __name__ == '__main__':
   unittest.main()
