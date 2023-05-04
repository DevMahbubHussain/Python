# conditional statment

n1 = input("Enter Number1")
n2 = input("Enter Number2")
n3 = input("Enter Number3")

if n1 > n2 and n1 > n3:
    print("Number1 {} is bigger than number2 {} and number3 {}".format(n1,n2,n3))
elif n2 > n3:
    print("Number2 {} is bigger than number1 {} and number 3".format(n2, n1,n3))
else:
    print("Number3 {} is bigger than number1 {} and number2 {}".format(n3, n1,n2))