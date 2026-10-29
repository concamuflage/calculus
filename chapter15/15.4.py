import sympy as sp
import numpy as np
import scipy.integrate as spint
import matplotlib.pyplot as plt

x= sp.Symbol('x')

f = sp.cos(2*sp.pi*x)* sp.exp(-x**2)
F = sp.integrate(f,x)

xx = np.linspace(-np.pi,np.pi,5001)
f_num = sp.lambdify(x,f)
f_val = f_num(xx)
f_int = spint.cumulative_trapezoid(f_val,xx,initial=0)
defint = spint.trapezoid(f_val,dx=xx[1]-xx[0])
plt.plot(xx,f_int)
plt.axhline(y=0,color='k')
plt.show()
plt.title(fr'A $\approx$ {defint:.25f}')
print(f_int[-1])
print(defint)