#function declartion
def binary_search(lists, item):
    for i in range(len(lists)):
        if lists[i] == item:
            print("{} is found index of {}".format(lists[i],i))
            return 1

    print("{} is not found ".format(lists[i]))
    return -1

l = (10, 20, 30, 40, 50) # list declartion

binary_search(l, 500) # function invoking
