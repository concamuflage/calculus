import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from numpy.ma.core import left_shift

x = sp.Symbol('x')
f = 1/((x-2)**2)
f_fun = sp.lambdify(x, f, 'numpy')

xx = np.linspace(0,4,100)
y = f_fun(xx)

plt.plot(xx,y,'o')
plt.show()

left = sp.limit(f, x, 2, dir='-')
right = sp.limit(f, x, 2, dir='-')
both =sp.limit(f, x, 2)

print(left)
print(right)
print(both)
