# break  continuee statment

cart = [10,30,400,500,600,60,70]

for item in cart:
    if item > 500:
        print("Insurance is required for this items ", item)
        break
    print(item)

    carts = [10, 30, 400, 500, 600, 60, 70]

    for items in cart:
        if items > 500:
            print("Insurance is required for this items ", items)
            continue
        print(items)

for i in range(4): # 0 to (n-1) (4-1) = 3  = 0,1,2
    for j in range(2):# 0 to (n-1) (2-1) = 3  = 0,1
        print(" i = " , i, 'j  =',j)
