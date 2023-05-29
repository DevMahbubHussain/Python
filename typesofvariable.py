#instance variable
class Studen:
    schoolName = 'Mahbub School' # static variable or class level

    def __init__(self,name,roll): # constructor
        self.name = name #instance variable or object level
        self.roll = roll #instance variable or object level

    def info(self):#instance method
        print('Name is ',self.name) # get value from instance variable
        print('Name is ',self.name) # get value from instance variable
        print('Roll is',self.roll) # get value from instance variable

    def test(self):
        x = 10 # is a local or temporary,method level variable
        print('School Name is',self.schoolName,x)


s = Studen('Mahbub',1001)
s.test()
