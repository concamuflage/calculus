import sympy as sp
import numpy as np
import scipy.integrate as spint
import matplotlib.pyplot as plt

x= sp.Symbol('x')
a= sp.Symbol('a')

n = 501
_,axes = plt.subplots(1,2)
aa = np.linspace(np.pi/10,6*np.pi,30)
xx = np.linspace(-20*np.pi,20*np.pi,n)

net_area = np.empty(30)
total_area = np.empty(30)
for i, a in enumerate(aa):
    f = sp.cos(a * x) * sp.exp(-x ** 2)
    f_num = sp.lambdify(x,f)
    if i % 9 == 0:
        axes[0].plot(xx, f_num(xx), color='red')
    net_area[i] = spint.trapezoid(f_num(xx),xx)
    total_area[i] = spint.trapezoid(np.abs(f_num(xx)),xx)

axes[0].set_xlim(-2,2)
axes[1].plot(aa,net_area,"s-")
axes[1].plot(aa,total_area,"o-")
plt.show()