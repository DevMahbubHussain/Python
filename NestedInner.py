class Outer:
    def __init__(self):
        print('Outer object')
    class Inner:
        def __init__(self):
            print('Inner Object')
        class InnerInner:
            @staticmethod
            def m1():
                print('Inner Inner Static method')




#Outer().Inner().InnerInner().m1()
Outer().Inner().InnerInner.m1()