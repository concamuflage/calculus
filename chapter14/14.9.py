import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import scipy.integrate as spint

_,axes = plt.subplots(1,2)

x = sp.Symbol('x')

p = 2*(x**3) -x**2 +4*x
q = 7*x**3+4*x**2-1
g = p/q
f = sp.exp(g)

g_num = sp.lambdify(x,g,'numpy')
f_num = sp.lambdify(x,f,'numpy')


a = -3
b = 2
n = 900
xx = np.linspace(a,b,n+1)

# remove the artificial vertical line at the discontinuity
f_values = f_num(xx)
# max_index = np.argmax(f_values)
# f_values[max_index -1] = np.nan
# left
axes[0].plot(xx,f_values,".")
axes[0].set_ylim(-2,30)



# right
axes[1].plot(xx,f_num(xx),"x")
axes[1].set_ylim(0,30)


# right side, wrong plot
# because the plot didn't consider the discontinuity point

# areas = spint.cumulative_simpson(yy,x = xx,initial=0)
# axes[1].plot(xx[:],areas,"o")

# right side, correct plot
# piecewise to skip the discontinuity

xx1 = xx[xx < 0.38]
xx2 = xx[xx > 0.5]
yy1 = f_num(xx1)
yy2 = f_num(xx2)
areas1 = spint.cumulative_simpson(yy1,x = xx1,initial=0)
areas2 = spint.cumulative_simpson(yy2,x = xx2,initial=0)
init1 = f_num(-3)
init2 = areas1[-1]+init1
# axes[1].plot(xx1,areas1+init1,"ko")
# axes[1].plot(xx2,areas2+init2,"ko")

axes[1].plot(xx1,areas1,"ko")
axes[1].plot(xx2,areas2,"ko")
axes[1].set_ylim(0,30)
plt.show()

