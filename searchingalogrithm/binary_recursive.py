def binary_search(data,low,high,item):
    if low <= high:
        middle = (low+high)//2

        if data[middle] == item:
            print("Found")
            return  middle
        elif data[middle] > item:
            return binary_search(data,low,middle-1,item)
        else:
            return binary_search(data,middle+1,high,item)

    print("Not found")
    return -1

data = (10,20,30,40,50,60)
low = 0
high = len(data)-1

binary_search(data,low,high,500)






