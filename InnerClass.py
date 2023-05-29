class Outer:
    def __init__(self):
        print('Outer Class Object')
    class Inner():
        def __init__(self):
            print('Inner class object')
        def m1(self):
            print('Inner class method')

o = Outer()
i = o.Inner()
i.m1()