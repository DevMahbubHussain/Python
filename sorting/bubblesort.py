def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0,n-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
    return data
print(bubble_sort([10,1,2]))
