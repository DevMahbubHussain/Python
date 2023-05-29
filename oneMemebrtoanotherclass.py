class Employee:
    def __init__(self,eno,ename,esal):
        self.eno = eno
        self.enam = ename
        self.esal = esal
    def display(self):
        print('Employee No ', self.eno)
        print('Employee Name',self.enam)
        print('Employee Salary',self.esal)


class Manager:
    def updateSalary(emp):
        emp.esal = emp.esal + 10000
        emp.display()

emp = Employee(101,'Mahbub',20000)
Manager.updateSalary(emp)