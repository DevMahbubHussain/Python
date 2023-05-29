try:
    try:
        print('Outer try block')
        print(10/0)
    except ZeroDivisionError:
        print("Inner Except block")
    finally:
        print('Inner Finally Block')
except:
    print('outer except block')
finally:
    print('outer finally blick')