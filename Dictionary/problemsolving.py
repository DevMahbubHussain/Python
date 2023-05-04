#problem 1

'''
d = eval(input("Enter dict"))
sum = 0
for item in d.items():
    sum = sum+item[1]
print("The sum :", sum)
'''
#problem 2

'''
word = input("Enter String")
d = {}
for ch in word:
    d[ch] = d.get(ch,0)+1
for k,v in d.items():
    print(k,"Occurs in",v,"Times")
'''
#problem 3
'''
word = input("Enter String")
vowels = {'a','e','i','o','u'}
d = {}

for item in word:
    if item in vowels:
        d[item] = d.get(item,0)+1
for k,v in sorted(d.items()):
    print(k,"Ocuured",v, "times")
'''
#problem 4 Student Managment System with Search Features
'''
n = int(input("Enter number of student"))
d = {}

for i in range(n):
    name = input("Enter student name")
    marks = int(input("Enter student marks"))
    d[name] = marks

print("student data insertion completed")
print("*" * 30)
print("Name",'\t\t','Marks')
print("*" * 30)

for k,v in d.items():
    print(k,'\t\t',v)
print("Search student name for marks : ")

while True:
    name = input("Enter student name for marks ")
    marks = d.get(name,-1)
    if marks == -1:
        print("Student Not found")
    else:
        print("The marks of ", name, "are", marks)
    option = input("Do you want to find another student another student marks[Yes?No]")
    if option.lower() == 'no':
        break
print("Thanks for using our application")
'''

# dict comprenshion
'''
d = {x:x*x for x in range(1,6)}
print(d)
'''

# list,set,tuplle merging
'''
l1 = [10,20]
l2 = [30,40]
l3 = [*l1,*l2]
print(l3)
'''

#dict mergin
d1 = {100:'A',200:'B'}
d2 = {300:'C',400:'D'}
d3 = {**d1,**d2}
print(d3)