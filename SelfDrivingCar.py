class SelfDrivingCar(object):

    def __init__(self):
        self.speed = 0

        self.destination = None

    def stop(self):
        self.speed = 0

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        if self.speed > 0:
            self.speed -= 1
