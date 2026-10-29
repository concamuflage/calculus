import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.Symbol('x',real=True)
f = x**2-0.5

_,axes = plt.subplots(2,1)
f_num = sp.lambdify(x,f,'numpy')

# dxs = np.arange(0.001,0.5,0.01) # mine
dxs = np.logspace(np.log10(.5),np.log10(.001),20) # book answer
areas = np.empty(len(dxs))
len_arr = np.empty(len(dxs))
bounds = [-0.5,1]
for i, dx in enumerate(dxs):

    xx = np.arange(bounds[0],bounds[1]+dx,dx)
    len_arr[i] = len(xx)
    areas[i] = np.sum(np.abs(f_num(xx)*dx))

analytical_area = 0.537
axes[0].plot(dxs,len_arr,'s')
axes[0].set_ylim(0, 10)
axes[0].set_xlim(0.2, 0.5)
axes[1].set_xscale('log')
axes[1].invert_xaxis()
axes[1].plot(dxs,areas,"o")
axes[1].axhline(analytical_area,color="r")
plt.show()
