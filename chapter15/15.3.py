import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import scipy as sip

_,axes = plt.subplots(1,2)

power = np.linspace(-3,-1.5,21)
x = sp.symbols('x')

cmap = plt.cm.gray
norm = plt.Normalize(power.min(), power.max())

xx = np.linspace(0.001,10,100)
for i, p in enumerate(power):
    color = cmap(norm(p))
    f = x**p
    F = sp.integrate(f,x)
    F_a = sp.limit(F,x,sp.oo)
    F_b = F.subs(x,1)
    integral = F_a - F_b
    f_num = sp.lambdify(x,f)
    axes[0].plot(xx,f_num(xx),color = color)



axes[0].set_ylim(0.0,1.0)

# right panel

xx2 = np.logspace(0,5,100)

for i, p in enumerate(power):
    color = cmap(norm(p))
    f = x**p
    f_num = sp.lambdify(x,f)
    yy = f_num(xx2)
    F2 = sip.integrate.cumulative_trapezoid(yy,xx2,initial=0)
    axes[1].plot(xx2,F2,color = color)
    axes[1].set_xscale('log')

sm = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
plt.colorbar(sm,ax=axes[1])
plt.show()
