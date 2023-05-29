class Car:
    def __init__(self,cname,cmodel,ccolor):
        self.cname = cname
        self.cmodel = cmodel
        self.ccolor = ccolor
    def getinfo(self):
        print("Car Name:{} Car Model:{} Car Color: {}".format(self.cname,self.cmodel,self.ccolor))

class Employee:
    def __init__(self,ename,eno,ecar):
        self.ename = ename
        self.eno = eno
        self.ecar = ecar
    def emInfo(self):
        print('Employee Name',self.ename)
        print('Employee no',self.eno)
        print('Employe Car Information are: ')
        self.ecar.getinfo()

car = Car('Honda','H45','green')
emp = Employee('Mahbub',22051,car)
emp.emInfo()