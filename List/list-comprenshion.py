l = [x*x for x in range(1,11)] # square 2
print(l)

l1 = [2**x for x in range(1,6)] # 2 power ** is exponential opetrator
print(l1)

l2 = [x for x in range(1, 101) if x % 10 == 0]

print(l2)


l3 = [10,20,30,40]
l4 = [30,40,50,60]
l5 = [x for x in l3 if x not in l4] # uncommon element
l6 = [x for x in l3 if x in l4] # common element
print(l5)
print(l6)

liss = ['Mahbub','Hussain','Mamun']
output =  [word[1] for word in liss]
print(output)


vowels = ['a','e','i','o','u']
word = input("Enter any word for search vowel")
# comprension why
ll = [ch for ch in vowels if ch in word]
print(ll)



result = []
for ch in word:
    if ch in vowels:
        if ch not in result:
            result.append(ch)


print("the numbers of voewl",len(result))
print(result)