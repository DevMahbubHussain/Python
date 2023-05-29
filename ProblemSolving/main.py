def findMaxvalue(a,b,c):
    max_value = a
    if  b > max_value :
        max_value = b
    if  c > max_value:
        max_value = c
    return max_value


output = findMaxvalue(10,20,30)
print(output);