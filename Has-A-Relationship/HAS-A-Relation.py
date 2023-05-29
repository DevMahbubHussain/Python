class Engine:
    def __init__(self):
        self.power = '150kw'
    def m1(self):
        print("Engine speace functionality")


class Car:
    def __init__(self):
        self.engine = Engine()
    def usecar(self):
        print("Car required engine functionality")
        self.engine.m1()
        print(self.engine.power)

c = Car()
c.usecar()