import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import scipy as sip

_,axes =plt.subplots(2,2)
x = sp.Symbol('x')
a = sp.sin(x)
b = sp.sin(a)**3
f1 = 10*sp.sin(b)**5
c = sp.cos(x)**2
d = sp.cos(c)**4
f2 = sp.cos(d)**6

f1_num = sp.lambdify(x,f1)
f2_num = sp.lambdify(x,f2)

xx = np.linspace(0,15,100)

axes[0,0].plot(xx,f1_num(xx),".")
axes[0,0].plot(xx,f2_num(xx),"x")

# plot 2
deri1 = sp.diff(f1,x)
deri2 = sp.diff(f2,x)
deri1_num = sp.lambdify(x,deri1)
deri2_num = sp.lambdify(x,deri2)
axes[0,1].plot(f1_num(xx),deri1_num(xx),".")
axes[0,1].plot(f2_num(xx),deri2_num(xx),".")

# plot 3

areas1 = sip.integrate.cumulative_trapezoid(f1_num(xx),xx,initial=0)
areas2 = sip.integrate.cumulative_trapezoid(f2_num(xx),xx,initial=0)
axes[1,0].plot(xx,areas1,".")
axes[1,0].plot(xx,areas2,".")

# plot 4
axes[1,1].plot(areas1,areas2,".")
plt.show()





