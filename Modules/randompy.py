from random import *

for i in range(10):
    print(random())
print("=========")

for j in range(10):
    print(uniform(5,10))
print("=========")

for jj in range(10):
    print(randint(1,10))

print("=========")

fruits = ['Apple','Mango','Bananna','orange','licho']
for iii in range(10):
    print(choice(fruits))