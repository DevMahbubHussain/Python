'''
print(__name__)
'''
'''
if __name__ == '__main__':
    print("direct Excution like a main application")
else:
    print("Indirect Execution bcz of import statment")

'''

def f1():
    print("f1")
def f2():
    print("f2")
def f3():
    print("f3")
if __name__ == '__main__':
    f1()
    f2()
    f3()