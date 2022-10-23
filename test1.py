import numpy as np
from sympy import*

ar = np.zeros(0)
array_5 = ar * 5
print(array_5)

ar_2 = np.array([2, 3])

extended_array = np.append(array_5, ar_2)
print(extended_array)
print(array_5)

x_coord = symbols('x_coord')

equation_1 = x_coord**2 + 5
b = equation_1.subs(x_coord , 10)
print(b)

foo = "bar_tender"
if foo.startswith('bar'):
    print('Yes')
