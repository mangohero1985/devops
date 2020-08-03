class Vehicle(object):
    def __init__(self):
        self.speed = 0

    def run(self):
        if self.speed > 0:
            print("A car is moving")
        else:
            pass
    
    def stop(self):
        if self.speed == 0:
            print("A car stops")
        else:
            pass
