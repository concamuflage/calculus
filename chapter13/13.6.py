import sympy as sp
import numpy as np

import matplotlib.pyplot as plt
from numpy.ma.core import left_shift

x = sp.Symbol('x')
f = x**4-0.5
a = -0.5
b = 1
n = 100
delta = (b-a)/n

xx = np.linspace(a,b,100)
f_num = sp.lambdify(x,f,'numpy')
f_vals = f_num(xx)

aa = np.linspace(a,b,n+1)
area = 0
for i in range(len(aa)-1):
    left = aa[i]
    right = aa[i+1]
    height_left = f.subs(x,left)
    height_right =f.subs(x,right)
    area += ((height_left+height_right)/2)*delta
    x_coordinates = [left,left, right,right]
    y_coordinates = [0,height_left,height_right,0]
    plt.fill(x_coordinates,y_coordinates,facecolor='none',alpha = 0.5, edgecolor='black')


ground_truth = sp.integrate(f,(x,a,b))

plt.plot(xx,f_vals)
plt.axhline(y=0,color='k',linestyle='--')
plt.show()

print(area)
print(ground_truth)


