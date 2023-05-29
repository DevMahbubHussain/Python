try:
    x = int(input('Enter first bumber'))
    y = int(input('Enter 2nd number'))
    print('The result',x/y)
except BaseException as msg:
    print("The type of exception",type(msg))
    print("The type of exception",msg.__class__)
    print("The type of exception", msg.__class__.__name__)
    print("The description of exception", msg)