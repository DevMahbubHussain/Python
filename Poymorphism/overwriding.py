class Parent:
    def property(self):
        print('Property')
    def marry(self):
        print('Parent Overriding')

class Child(Parent):
    def marry(self):
        super().marry()
        print('Child Overriding')

c  = Child()
c.property()
c.marry()