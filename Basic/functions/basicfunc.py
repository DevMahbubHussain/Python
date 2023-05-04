'''
def calculate(a, b):
    print("Sum", a + b)
    print("diff", a - b)
    print("Mul", a * b)


calculate(10, 20)

calculate(100, 20)
'''

def factorial(num):
    result = 1
    while num >=1:
        result = result*num
        num = num - 1
    return  result


for i in range(1,6):
    print("Factorial of {} : ".format(i), factorial(i))


