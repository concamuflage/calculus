import sympy as sym
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt


x = sym.Symbol('x',real=True)
f = x**3/(sym.exp(x)-1)
f_num = sym.lambdify(x,f)

xx = np.linspace(-1,3,100)
integral = sym.integrate(f,(x,1,3))
integral_2,error = sp.integrate.quad(f_num,-1,3)
print(integral)
print(integral_2)
plt.plot(xx,f_num(xx))
plt.show()