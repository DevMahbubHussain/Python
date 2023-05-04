def calculate(a,b):
    print("Sum : ", a + b)
    print("subtraction : ", a-b)

calculate(10, 10)

def wish(name):
    print("Hell", name, "Good Evening")

wish('Mahbub')

def squareit(number):
    sq = number * number
    print("The square of {} is : {}".format(number,sq))

squareit(5)

# multiple values returns from a function

def sum_sub(a,b):
    adddition = a + b
    subtraction = a - b
    return adddition,subtraction

# x,y = sum_sub(100,50)
t = sum_sub(100,50)
# print("Summation: ", x)
# print("subtraction: ", y)

for i in t:
    print(i)