class Studen:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    def __str__(self):
        return 'Name:{} Roll : {} Marks : {}'.format(self.name,self.roll,self.marks)

s = Studen('Mahbub',101,95)
print(s)