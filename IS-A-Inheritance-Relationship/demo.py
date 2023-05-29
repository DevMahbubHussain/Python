class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eatdrink(self):
        print('Eating & drinking')

class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno = eno
        self.esal = esal
    def work(self):
        print('Working on it Python')
    def eminfo(self):
        print(self.name)
        print(self.age)
        print(self.eno)
        print(self.esal)

emp = Employee('Mahbub',31,1010,50000)
emp.eatdrink()
emp.work()
emp.eminfo()