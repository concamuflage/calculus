import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import scipy as sip

x = sp.Symbol('x')
f = sp.exp(-x**2)/sp.exp(x+1)

f_num = sp.lambdify(x,f)

xx = np.linspace(-3,2,100)
delta = xx[1] - xx[0]
delta2 = xx[2] - xx[0]

plt.plot(xx,f_num(xx))
f_values = f_num(xx)
areas1=sip.integrate.cumulative_trapezoid(f_values,dx = delta)
areas2 = sip.integrate.cumulative_trapezoid(f_values,dx = delta2)
plt.plot(xx[1::3],areas1[::3],linestyle = '--')
plt.plot(xx[1::3],areas2[::3],linestyle = 'dotted')
plt.show()
