'''
d = {'name': 'Mahbub', 'age': 30}

print(d)


l = [(100,'a','ami'),(200,'b','tumi'),(300,'c','kk')] # not allow
'''
l = [(100,'a'),(200,'b'),(300,'c')] #allow
'''
d = dict(l)
print(d)


dd = {100:'Ami'}
dd[300]='tumi'
dd[100]='hello'
del dd[100]
print(dd)

print(dd)
'''

dic = {}
n = int(input("Enter the no of student"))
for i in range(n):
    name = input("Enter the student name")
    marks = input("Enter the student marks")
    dic[name] = marks

print("*" * 30)
print("Name","\t\t","Marks")
print("*" * 30)

for name in dic:
    print(name,"\t\t",dic[name])
