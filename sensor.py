from vehicle import Vehicle
from person import Person
class Sensor(object):
    def __init__(self):
        self.car = Vehicle()
        self.pedestrian = Person()

    def detect(self, speed):
        if speed >= 20:
            return self.car
        else:
            return self.pedestrian
