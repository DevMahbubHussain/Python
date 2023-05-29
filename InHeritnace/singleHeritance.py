class P:
    def m1(self):
        print('Parent Class method')

class C(P):
    def m2(self):
        print('Child Class')

c = C()
c.m1()
c.m2()