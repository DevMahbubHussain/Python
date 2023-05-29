class Test:

    @staticmethod
    def m1():
        print('I am Static method')

    @staticmethod
    def add(a,b):
        print('Sum',a+b)

Test.m1();
Test.add(10,20)