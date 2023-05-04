def  sum(*n):
    total = 0
    for n1 in n:
        total = total + n1
    print("The Sum : ", total)

sum()
sum(10,10)
sum(100,1)


def f1(x,*y):
    print(x)
    for y1 in y:
        print(y1)

f1(0)
f1(10,20)