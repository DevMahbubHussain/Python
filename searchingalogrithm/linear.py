def linear_search(data,item):
    for i in range(len(data)):
        if data[i] == item:
            print("Found")
            return 1
    print("Not Found")
    return -1

data = (10,20,30,40,50)

linear_search(data,100)