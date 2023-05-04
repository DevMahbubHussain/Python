s = lambda n: n*n
print(s(4))

# filter with lambda functio
l = [1,2,3,4,5,6,7,8,9,10]

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

# li = list(filter(isEven,l))
l1 = list(filter(lambda n:n%2==0,l))
print(l1)

# map function with lamda function

ll = [1,2,3,4,5]

def squareIT(n):
    return n*n

# output = list(map(squareIT,ll))
output = list(map(lambda n:n*n,ll))

print(output)

#multiple list in map
la = [1,2,3,4,5]
lb = [5,10,15,20,25]
l3 = list(map(lambda x,y:x+y,la,lb))
print(l3)

#reduces functions

from functools import *
lr = [10,20,30,40,50,60]
result = reduce(lambda x,y:x+y,lr)
print(result)
