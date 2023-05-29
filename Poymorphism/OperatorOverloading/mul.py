class Employee:
    def __init__(self,name,salaryPerDay):
        self.name = name
        self.salaryPerDay = salaryPerDay

    def __mul__(self, other):
        return self.salaryPerDay * other.workingDays

class Timsheet:
        def __init__(self,name,workingDays):
            self.name = name
            self.workingDays = workingDays


e = Employee('Mahbub',500)
t = Timsheet('Mahbub',25)

print('Salary',e*t)