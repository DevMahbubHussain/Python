class Test:
    def __init__(self):
        self._x = 10
    def _m1(self):
        print('Protected method')

    def _m2(self):
        print(self._x)
        self._m1()

class SubTest(Test):
    def m3(self):
        print(self._x)
        self._m1()
        self._m2()

sub = SubTest()
sub.m3()
print(sub._x)