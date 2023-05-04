def binary_search(data,item):
    low = 0
    high = len(data)-1

    while low <= high :
        middle = (low+high)//2

        if data[middle]==item:

            print("Found {}".format(data[middle]))

            return 1

        elif data[middle] > item:

            high = middle-1
        else:
            low = middle + 1

    print("Not found")

    return -1

data = (10,20,30,40,50,60,700)

binary_search(data,700)
