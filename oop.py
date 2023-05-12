'''
class Student:
    def __init__(self):
        self.name = 'Mahbub Hussain'
        self.rollNo = 101
        self.marks = 90
    def talk(self):
        print('My name is ', self.name)
        print('My Roll is ',self.rollNo)
        print('My Marks are',self.marks)

s = Student()
print(s.name)
print(s.rollNo)
print(s.marks)
s.talk();
'''

class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    def talk(self):
        print('Hello, My Name is ', self.name)
        print('My Roll is',self.roll)
        print('My Marks is ' ,self.marks)

s1 = Student('Mahbub',101,90)
s2 = Student('Hussain',102,95)

s1.talk()
s2.talk()

class Test:
    def __init__(self):
        print('Constructor')
    def m1(self,x):
        print('x value is',x)
t = Test()
t.m1(10)

class Test1:
    def t1(self):
        print('Hello without Constructor')

tt = Test1()
tt.t1();