import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import scipy as sip

x = sp.Symbol('x')
f = (2*(x**2) - 3*x)/sp.sqrt(x**2-x+1)
integral = sp.integrate(f,x)

f_num = sp.lambdify(x,f)
integral_num = sp.lambdify(x,integral)

xx = np.linspace(-2,5,100)

plt.plot(xx,integral_num(xx))
plt.plot(xx,f_num(xx),linestyle = '--')


# approximation

areas = []
n = 30
breakpoints = np.linspace(-2,5,n )
# assuming area = 0 makes estimated curve higher than the analytical curve with c = 0
# also it implies the accumulation of areas from -infinity to -2 = 0,which might not be correct.

# area = 0

area = float(integral_num(-2))
areas.append(area)
for i in range(n-1):
    x_pairs = breakpoints[i:i+2]
    y_pairs = f_num(x_pairs)
    area += sip.integrate.trapezoid(y_pairs,x_pairs)
    areas.append(area)


areas = np.array(areas)
plt.plot(breakpoints,areas,"s")

plt.show()
