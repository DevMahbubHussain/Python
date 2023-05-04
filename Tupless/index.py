t = (10,20,30,40,50,60,70,80,0,5,1)
so = sorted(t,reverse=True) # fo decending order
asc = sorted(t) # acending order
newt = tuple(so)
print(t)
print(newt)
r = reversed(t)
t1 = tuple(r)
print(t) # original tuple
print(t1) # reversed tuple
print(t[::2])
print(t[2:5:2])
print(t[2:5])


inputu = eval(input("Enter tuple of numbers : "))
suma = 0;
lendata = len(inputu)

print(sum(inputu))
print("Average",sum(inputu)/lendata)


for x in inputu:
    suma = suma + x
print("the sum " , suma)
print("Average : ",suma/lendata)


