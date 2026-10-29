import numpy as np
import sympy as sp
from matplotlib import pyplot as plt

phi = sp.Symbol('phi')

f = sp.cos(phi)
fd = sp.diff(f, phi)

f_num = sp.lambdify(phi,f)
fd_num = sp.lambdify(phi,fd)

dx = 0.01
x = np.arange(-1.5*np.pi, 1.5*np.pi+dx, dx)

dx1 = 0.1
x1 = np.arange(-1.5*np.pi, 1.5*np.pi+dx1, dx1)
y1 = [float(fd.subs(phi,num)) for num in x1]

plt.plot(x, f_num(x))
plt.plot(x, fd_num(x))
plt.plot(x1, y1,"ro")

plt.legend()
# plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],labels=[r'$-\pi$',r'$-\pi/2$','0',r'$\pi/2$',r'$\pi$'])
plt.xlabel(r'$\phi\; (rad.)$')
plt.xlim(x[[0,-1]])
plt.show()



