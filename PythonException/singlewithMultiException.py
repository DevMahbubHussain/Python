try:
    x = int(input('Enter first bumber'))
    y = int(input('Enter 2nd number'))
    print('The result',x/y)
except(ZeroDivisionError,ValueError) as msg:
    print(msg)


