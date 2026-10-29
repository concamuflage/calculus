import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import scipy as sip

_,axes = plt.subplots(2,2)
x = sp.Symbol('x')
g = sp.sin(x)+2
f1 = 1/(sp.sqrt(x)*g)
f2 = 1/(x**2*g)

f1_num = sp.lambdify(x,f1)
f2_num = sp.lambdify(x,f2)

xx = np.linspace(1,30,100)

f1_vals = f1_num(xx)
f2_vals = f2_num(xx)

areas1 = sip.integrate.cumulative_trapezoid(f1_vals,xx,initial=0)
areas2 = sip.integrate.cumulative_trapezoid(f2_vals,xx,initial=0)

axes[0,0].plot(xx,f1_vals)
axes[0,0].plot(xx,f2_vals)
axes[0,1].plot(xx,areas1)
axes[0,1].plot(xx,areas2)

result1 = sp.integrate(f1,(x,sp.pi,sp.oo))
result2 = sp.integrate(f2,(x,sp.pi,sp.oo))

print(float(result1))
print(float(result2))

# max normalize
axes[1,0].plot(xx,f1_vals/np.max(f1_vals))
axes[1,0].plot(xx,f2_vals/np.max(f2_vals))
axes[1,1].plot(xx,areas1/np.max(areas1))
axes[1,1].plot(xx,areas2/np.max(areas2))
plt.show()




