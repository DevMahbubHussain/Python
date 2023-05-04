s = set()
s.add(10)
s.add('Mahbub')
print(s)
ss = {10,0,0,0}
print(type(ss))
print(ss)

sss = set(range(0,101,10))
print(sss)

st = {10,20,30}
st.add(100)
print(st)

stup = {10,20,30}
l = [200,300,400]
stup.update(l)
print(stup)
stup.update(range(1,101,10),'Mahbub')
print(stup)

# write a program to elimniate duplicate present in the list
#aprroch one
ll = [1,1,2,3,3,3,4,4,5]
stt = set(ll)
result = list(stt)
print(result)

#aprroch two

l3 = []
for x in ll:
    if x not in l3:
        l3.append(x)
print(l3)

# write a program to print different vowels present in the given word

word = input("Enter word to search vowel")
s = set(word)
v = {'a','e','i','o','u'}
d = s.intersection(v)

print(d)