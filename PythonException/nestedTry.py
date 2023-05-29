try:
    x = int(input('Enter first bumber'))
    y = int(input('Enter 2nd number'))
    print('The result',x/y)
except ArithmeticError:
    print("Arithmatic Error")
except ZeroDivisionError:
    print("Can't divide in zero")
except ValueError:
    print("Please Provide Only int value ")


