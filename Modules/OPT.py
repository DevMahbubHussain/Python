from random import *
print(randint(0,9),randint(0,9),randint(0,9),
randint(0,9),randint(0,9),randint(0,9), sep='')
otp = ''
for i in range(6):
    otp = otp + str(randint(0,9))
print(otp)
print("===========")

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
print(choice(alpha),choice(digits),
choice(alpha),choice(digits),choice(alpha),choice(digits),sep='')
