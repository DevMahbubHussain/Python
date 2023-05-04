l1 = [10,20,3,50,60]
l2 = l1[::]
l3 = l1.copy()


print(id(l1))
print(id(l2))
print(id(l3))


ll = [[10,20,30],[40,50,60],[70,80,90]]
for x in ll:
    print(x)

for x in ll:
    for y in x:
        print(y,end=' ')
    print()


