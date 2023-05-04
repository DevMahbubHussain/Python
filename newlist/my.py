'''l  = [10,10,20,30,40,50]
x = int(input("Enter the value you want remove"))
if x in l:
    l.remove(10)
else:
    print(x,"not avilable")
print(l)
'''
x = [1,1,1,2,2,2,3,3,3]
y = int(input("Enter your removal data"))

while True:
    if y in x:
        x.remove(y)
    else:
        break
print("after removal",x)



ll = [10,20,30,60]
ll.clear()
print(ll)