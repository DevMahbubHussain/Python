# There are 3 types of variables are allowed.

# Instance Variables (Object Level Variables)
# Static Variables (Class Level Variables)
# Local variables (Method Level Variables)

# Within the Python class, we can represent operations by using methods.
# The following are
# various types of allowed methods

# Instance Methods
# Class Methods
# Static Methods

# What is Reference Variable?
# The variable which can be used to refer object is called reference variable.
# By using reference variable, we can access properties and methods of object.

# Self Variable:
# self is the default variable which is always pointing to current object
# (like this keyword in Java)
# By using self we can access instance variables and instance methods of object.
#  self should be first parameter inside constructor
# def __init__(self)
# self should be first parameter inside instance methods
# def talk(self):

# Instanace Variable
# Inside Constructor by using self variable
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        print('summation',self.a + self.b)

t = Test()


# Inside Instance Method by using self variable

class Test1:
    def m1(self):
        self.a = 100
        self.b = 200
        print('Subtraction',self.a - self.b)
T1 = Test1()
T1.m1()

# Outside of the Class by using Object Reference Variable
class Test2:
    def __init__(self):
        self.a = 500
    def m1(self):
        self.c = 600

TT = Test2()
TT.d = 6000  # Outside of the Class by using Object Reference Variable

print(TT.d)

# Static Variables:
# If the value of a variable is not varied from object to object,
# such type of variables we
# have to declare with in the class directly but
# outside of methods. Such types of
# variables are called Static variables.

# For total class only one copy of static variable will be created
# and shared by all objects of that class.
# We can access static variables either by class name
# or by object reference. But recommended to use class name.


class StaticVariable:
    a = 10

    def __init__(self):
        # print(self.a)
        print(StaticVariable.a)
    def m2(self):
        # print(self.a)
        print(StaticVariable.a)
    @classmethod
    def m1(cls):
        # print(cls.a)
        print(StaticVariable.a)
    @staticmethod
    def m3():
        print(StaticVariable.a)

ss = StaticVariable()
ss.m1()










