class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print('Hi',self.name)
        print('Marks',self.marks)
    def grade(self):
        if self.marks>=60:
            print('You Got First class')
        elif self.marks>=50:
            print('You Got Second Class')
        elif self.marks>=35:
            print('You got 3rd grade')


n = int(input('Enter the Number of student'))
for i in range(n):
    name = input('Enter Student Name')
    marks = int(input('Enter Student Marks'))
    s = Student(name,marks)
    s.display()
    s.grade()
    print()

