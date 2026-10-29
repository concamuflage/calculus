import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import scipy as sip

_,axes = plt.subplots(2,2)
x = sp.Symbol('x')
f = sp.sin(x)/x
f_num = sp.lambdify(x,f)
xx = np.linspace(-40,40,1000)
f_vals = f_num(xx)

# derivative
xx2 = np.arange(-14*np.pi,14*np.pi,0.01)
areas = sip.integrate.cumulative_trapezoid(f_num(xx2),xx2,initial=0)

axes[0,0].plot(xx,f_vals,".")
axes[0,1].plot(xx2,areas,".")

# second part
xx3 = np.arange(-0.1,1,0.01)
f_vals3 = f_num(xx3)
areas3 = sip.integrate.cumulative_trapezoid(f_vals3,xx3,initial=0)
axes[1,0].plot(xx3,f_vals3,".")
axes[1,1].plot(xx3,areas3,".")


plt.show()

left_index = np.argmin(abs(xx3))
# abs(xx-1) is the distance to 1. which is the index closest to 1?
right_index = np.argmin(abs(xx3-1))
result1= sp.integrate(f,(x,0,1)).evalf()
result2 = areas3[right_index]-areas3[left_index]

print(result1)
print(result2)