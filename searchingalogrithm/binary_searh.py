#The Binary Search algorithm takes :
#data -  list or Tuple
#item - A item we wish to find in the list (data)

def binary_search(data,item):
    # set the initial bounds for the interval
    # The lower bound is the first index in the list
    # The upper bound is the last index in the list

    low = 0
    high = len(data) - 1

    # while interval is valid

    while low <= high:
        # find the middle item of the inerval
        midd = (low + high) // 2

        if data[midd] == item:
            print("item found {}".format(data[midd]))
            return midd

        elif data[midd] > item:

            high = midd-1

        else:
            low = midd + 1

    print("item not found {}".format(data[midd]))
    return -1

data = (10,20,30,40,50,60,70)

binary_search(data,70)

