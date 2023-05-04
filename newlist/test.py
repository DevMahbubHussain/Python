listss = []

listss.append(1)
listss.append(2)
listss.append(3)
listss.append(4)
listss.append(5)

print(listss)
print(len(listss))


li = [0,1,2,3,4,5,6,7,8,10]

for n1 in li:
    if n1%2 == 0:
        print(n1)

'''
i = 0

while i < len(li):
    print(li[i])
    i = i+1
'''


l = ["A","B","C"]
x = len(l)
for i in range(x):
    print(l[i],"is avilale at possitive index: ",i,"and at negative index: ",i-x)



lis = []
for i in range(101):
    if i % 10==0:
      lis.append(i)

print(lis)

mylist = [1,2,3]
mylist.insert(1,10)
print(mylist)

order1 = ['chicken','Burger']
order2 = ['Mutton','beef']
order1.extend(order2)
order2.extend(order1)
print(order2)
print(order1)

ll = [1,2,2,2,3,3]
print(ll.pop())

ll.remove(2)
ll.remove(2)
ll.remove(2)
print(ll)

x = int(input("Eneter element for find:"))
if x in ll:
    print('{} present at index {} '.format(x,ll.index(x)))
else:
    print(x,'Not avilable in the list')

ll3 = [1,2,2,2,3,3]
print(ll3.pop())
print(ll3)

nn = [10,20,30,40,50]
nn.reverse()
print(nn)

ss = [102,50,1,0]
ss.sort()
print(ss)
dd = ['dog','cat','apple']
dd.sort()
print(dd)