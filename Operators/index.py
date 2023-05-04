# relational operator

a = 10
b = 20


x = 0
y = 100
print(a<b)

l1 = [10,20,30]
l2 = [10,20,30]
print(l1 is l2)
print(l1==l2)

print(True and True)
print(True and False)
print(False and False)
print(False and True)

print("===========")
print(True or True)
print("===========")
print(True or False)
print("===========")
print(False or False)
print("===========")
print(False or True)
print("===========")
print("===========")

print(a and b)
print(x or y)

print("=========== Ternary operator ===============")

num1 = int(input("enter the first number"))
num2 = int(input("enter the 2nd number"))
num3 = int(input("enter the 3rd number"))

max = num1 if num1 > num2 and num1 > num2 else num2 if num2 > num3 else num3
print("Max number is : ", max)

