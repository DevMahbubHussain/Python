print('Stat1')

try:
    print(10/0)
except ZeroDivisionError as msg:
    print("The type of exception",type(msg))
    print("The type of exception",msg.__class__)
    print("The type of exception", msg.__class__.__name__)
    print("The description of exception", msg)
print('State2')