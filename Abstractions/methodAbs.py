from abc import abstractmethod,ABC
class Vehicle(ABC):
    @abstractmethod
    def getInfoWhile(self):
        pass

class Bus:
    def getInfoWhile(self):
        return 6
class Auto:
    def getInfoWhile(self):
        return 3


# v = Vehicle() Can't instantiate
# abstract class Vehicle with abstract method getInfoWhile

b = Bus()
print(b.getInfoWhile())
a = Auto()
print(a.getInfoWhile())