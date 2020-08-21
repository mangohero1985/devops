class Person(object):
    def __init__(self):
        self.speed = 0

    def walk(self):
        if self.speed <= 5 and self.speed > 0:
            print("A person is walking")
        else:
            pass

    def run(self):
        if self.speed > 5:
            print("A person is running")
        else:
            pass

    def stand(self):
        if self.speed == 0:
            print("A person is standing")
        else:
            pass
