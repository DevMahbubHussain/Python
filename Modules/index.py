'''import mahbubmathmodule
a = mahbubmathmodule.x
b = mahbubmathmodule.y
print("Output is A ", a)
print("Output is B ", b)
mahbubmathmodule.add(10,20)
mahbubmathmodule.product(10,20)

'''

from mahbubmathmodule import add as sums, x as a, y as b, product as multi
from test import f1
print(a)
print(b)
print(sums(10,20))
print(multi(10,5))
f1(10,20)

