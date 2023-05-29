class Test:
    def __init__(self):
        self.__x = 10
    def __m1(self):
        print('Private method')
    def m2(self):
        print(self.__x)
        self.__m1()

t = Test()
t.m2()

# way to access private variable & method
print(t._Test__x)
t._Test__m1()