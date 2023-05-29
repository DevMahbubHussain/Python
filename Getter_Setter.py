class Students:
    def setName(self,name):
        self.name = name
    def setMarks(self,marks):
        self.marks= marks

    def getName(self):
        return self.name

    def getMarks(self):
        return self.marks



n = int(input('Enter No of Students'))

studentList = []

for i in range(n):
    s = Students()
    name = input('Enter Student Name')
    marks = int(input('Enter Marks'))
    s.setName(name)
    s.setMarks(marks)
    studentList.append(s)

for s in studentList:
    print('Hello',s.getName())
    print('Your Marks', s.getMarks())
    print()



