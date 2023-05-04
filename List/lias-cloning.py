l1 = [10,20,30,40]
#l2 = l1[::]
l2 = l1.copy()

l1[1]= 777
print(l1)
print(l2)
print(id(l1))
print(id(l2))
print(l1 is l2)


'''l2 = l1

print(l2)
print(l1)
print(l1 is l2)'''