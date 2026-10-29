import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import scipy as sip

# this is the second version
# using sip.trapezoid directly

x = sp.Symbol('x')
f = (2*(x**2) - 3*x)/sp.sqrt(x**2-x+1)
integral = sp.integrate(f,x)

f_num = sp.lambdify(x,f)
integral_num = sp.lambdify(x,integral)

n = 100
xx = np.linspace(-2,5,n+1)
delta = xx[1] - xx[0]

plt.plot(xx,integral_num(xx))
plt.plot(xx,f_num(xx),linestyle = '--')

# approximation

areas = np.empty(len(xx))
# assuming area = 0 makes estimated curve higher than the analytical curve with c = 0
# also it implies the accumulation of areas from -infinity to -2 = 0,which might not be correct.

# area = 0
init= float(integral_num(-2))
f_values = f_num(xx)
for i in range(n+1):
    areas[i] = sip.integrate.trapezoid(f_values[:i+1],dx = delta)

#

areas2=sip.integrate.cumulative_trapezoid(f_values,dx = delta)


areas = np.array(areas)
plt.plot(xx[::3],areas[::3]+init,"s")
plt.plot(xx[::3],areas2[::3]+init,"b")
plt.show()
