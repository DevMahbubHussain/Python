class P1:
    def m1(self):
        print('Parent 1 method')

class P2:
    def m2(self):
        print('Parent 2 method')

class C(P1,P2):
    def m3(self):
        print('child method')

c = C()
c.m1()
c.m2()
c.m3()