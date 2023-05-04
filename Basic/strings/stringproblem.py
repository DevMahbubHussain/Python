'''s = 'ABCABCABCA'
i = s.find('ABC')
print(i)
i = s.find('ABC',3,10)
print(i)
i = s.find('ABC',6,10)
print(i)
i = s.find('ABC',9,10)
print(i)

print(s.count('ABC'))
'''
'''
s = 'ABCABCABCA'
substr = input("Enter your Sub String")
i = s.find(substr)
if i==-1:
    print("Not found")
c = 0
while i!= -1:
    print('{} is found in index of {}'.format(substr,i))
    c = c+1
    i = s.find(substr,i+len(substr),len(s))
print("Total index found",c)
'''
'''
s = 'ABC ABC ABCA'
s1 = s.replace(' ','')
print("The total spaces",len(s)-len(s1))
'''
'''
s = "Mahbub Hussain Mamun"
l = s.split();
for i in l:
    print(i)
print(l)

s = "02-12-2023"
l = s.split('-')
for x in l:
    print(x)

n = ['Mahbub','Hussain','Mamun']
j = ' * '.join(n)
print(j)

str1 = 'learning Python is very Easy'

print(str1.upper())
print(str1.lower())
print(str1.swapcase())
print(str1.title())
print(str1.capitalize())

m1 = input("enter the 1st string").lower()
m2 = input("enter the 2st string").lower()
if m1 == m2:
    print("they are equal")
else:
    print("Not equal")

nn = input("Enter the string")
nn1 = nn[0].upper()
nn2 = nn[1:len(s)+1].lower()
nn3 = nn[-1].upper()

print(nn1+nn2+nn3)

'''

str = input('Enter any charcter : ')
if str.isalnum():
    print("Alpha Numeric Charcters")
if str.isalpha():
    print("Alpha  Charcters")
if str.lower():
    print("Lower Case Charcters")
if str.isdigit():
    print("Only Digits")
else:
    print("Nothing")