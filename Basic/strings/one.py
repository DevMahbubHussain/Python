'''
print("Mahbub" + " " + "hussain")
print("Mahbub" *  3)
'''
'''
mains = input("enter the main string")
substr = input("Enter the substr")
if substr in mains:
    print("{} String is found in {}".format(substr, mains))
else:
    print("{} String is not found in {}".format(substr, mains))
'''
'''
s1 = input("enter the 1st string")
s2 = input("enter the 2st string")

if s1 == s2:
    print("Both are equal")
elif s1 < s2:
    print("less")
else:
    print("Greater")
'''
'''
s1 = input("enter the 1st string").strip()
if s1 == "Dhaka":
    print("I am from Dhaka")

elif s1 == "Sylhet":
    print("I am from Sylhet")
else:
    print("Not found")
'''

mail = input("Enter tha mail")
try:
    i = mail.index('@')
    print("@ symbol is required")
except ValueError:
    print("Invalid Email Address")