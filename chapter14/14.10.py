import sympy as sp
import numpy as np
import scipy as sip

import matplotlib.pyplot as plt

_,axes = plt.subplots(1,3)

x = sp.Symbol('x')
y = x**2 + sp.cos(x) +x

y_num = sp.lambdify(x,y,'numpy')

xx1 = np.linspace(-2,4,100000)
xx2 = np.random.uniform(-2,4,100000)
xx2.sort()
x_index = np.arange(len(xx1))


delta_1 = np.diff(xx1)
delta_2 = np.diff(xx2)

axes[0].plot(x_index,xx1,"r.")
axes[0].plot(x_index,xx2,"r.")

axes[1].plot(x_index[1:],delta_1,"r.",alpha=0.5)
axes[1].plot(x_index[1:],delta_2,"g.",alpha=0.5)



ground = sp.integrate(y,(x,-2,4))

yy1 = y_num(xx1)
yy2 = y_num(xx2)

axes[2].plot(xx1,yy1,"r.",alpha=0.3)
axes[2].plot(xx2,yy2,"g.",alpha=0.3)
axes[2].set_xlim(-2,4)

estimate1 = sip.integrate.simpson(yy1, x = xx1)
estimate2 = sip.integrate.simpson(yy1[1:], dx = delta_1[0])
estimate3 = sip.integrate.simpson(yy2, x = xx2)

plt.show()
print(float(ground))
print(estimate1)
# print(estimate2)
print(estimate3)





