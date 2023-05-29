class P:
    def m1(self):
        print('Parent Class method')

class C1(P):
    def m2(self):
        print('Child Class')

class C2(P):
    def m3(self):
        print('Child2 Class')

c = C1()
c.m2()
c.m1()

CC = C2()
CC.m3()
CC.m1()

