a = 10 # decimal base 10 0 to 9
b = 0b100 # binary base 2 0 to 1
print(type(b))
print(type(a))

print("=======")
c = 0o113 # octal base 8 0 to 7
print(type(c))

d = 0X12 # Hexadecimal base 16 0 to 15
print(type(d))

print("======= Float Data type===========")

f = 10.25
print(type(f))


# type conversion

data = 10.5
ok = True
oo = False
print(int(data))
print(int(ok))
print(int(oo))


s1,s2 = [int(x) for x in input("Enter 2 numbers").split()]

print("The summation",s1+s2)



print("Hello", " ",  end='')
print("Hello", " ", end='')
print("Hello", " ", end='')

print()

a,b,c = 10,20,30
print(a,b,c,sep=" : ")



dd = 10

print('a value %i' %dd)

name = 'mahbub'
marks = [20,30,40,50,60]
print('Your name is %s, Your Marks is : %s' %(name,marks))

price = 70.56789

print('Price value is = {}'.format(price))
print('Price value is = %.2f' %price)
