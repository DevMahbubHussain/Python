l = [10, 20, 30, 50, 40, 60, 9]


"""for i in l:
    if i % 2 == 0:
        print('Even')
    else:
        print('odd')"""


i = 0
while i < len(l):
    print("The Element present at +ve index :{} and at -ve index:{} is : {}".format(i, i-len(l),l[i]))
    i = i + 1
