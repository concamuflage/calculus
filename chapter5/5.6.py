import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
x = sp.Symbol('x')
f = x**2
fd = sp.diff(f,x)

x1,x2, x3 = 1,3,8
y1,y2,y3 = f.subs(x,x1), f.subs(x,x2), f.subs(x,x3)

# slopes
tangent_slope = fd.subs(x,1)
secant_slope = (y3-y2)/(x3-x2)

# the lines
y_secant = secant_slope*(x-x2)+y2
y_tangent = tangent_slope*(x-x1)+y1

f_num = sp.lambdify(x,f,'numpy')
y_secant_num = sp.lambdify(x,y_secant,'numpy')
y_tangent_num=sp.lambdify(x,y_tangent,'numpy')

x = np.linspace(-5,5,100)
plt.plot(x,f_num(x))
plt.plot(x,y_secant_num(x))
plt.plot(x,y_tangent_num(x))
plt.show()






