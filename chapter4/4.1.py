import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from numpy.ma.core import left_shift

n = 100
x = np.linspace(-2.5,2.5,n)
y = np.cos(x**2)**2+np.pi

x_sym = sp.Symbol('x')
y_sym = sp.cos(x_sym**2)**2+sp.pi

plt.plot(x,y)


left = 0
right = 2
left_x =[]
right_x =[]
left_values =[]
right_values =[]
for num in range(10):
    left_x.append(left)
    left_values.append(float(y_sym.subs(x_sym, left)))
    right_x.append(right)
    right_values.append(float(y_sym.subs(x_sym, right)))
    left += (1-left)/2
    right -= (right-1)/2

for x,y in zip(left_x,left_values):
    print("left")
    print(x,y)

for x,y in zip(right_x,right_values):
    print("right")
    print(x,y)

plt.plot(left_x,left_values,'ro')
plt.plot(right_x,right_values,'ro')
plt.show()



