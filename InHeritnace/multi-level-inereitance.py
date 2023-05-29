class P:
    def m1(self):
        print('Parent Class method')

class C(P):
    def m2(self):
        print('Child Class')
class CC(C):
    def m3(self):
        print('Subclass Method')

c = CC()
c.m1()
c.m2()
c.m3()