import sympy as sp
import numpy as np
import scipy.integrate as spint
import matplotlib.pyplot as plt

x= sp.Symbol('x')
a= sp.Symbol('a')

n = 21
aa = np.linspace(1/2,4*np.pi,n)
xx = np.linspace(-np.pi/2,np.pi/2,n)

f = sp.cos(a * x) * sp.exp(-x ** 2)
g = sp.sin(a * x) * sp.exp(-x ** 2)

area_f = sp.integrate(f,(x,-sp.oo,sp.oo))
area_g = sp.integrate(g,(x,-sp.oo,sp.oo))

area_f_num = sp.lambdify(a,area_f)
area_g_num = sp.lambdify(a,area_g)

areas_f = area_f_num(aa)
areas_g = area_g_num(aa)

print(areas_f)
print(areas_g)

plt.plot(aa,areas_f,'o')
plt.show()


