import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
x = sp.Symbol('x')
y = x**3/3+100*sp.sqrt(sp.Abs(x))
y_l = sp.lambdify(x,y,'numpy')

xx = np.linspace(10,-10,100)
plt.plot(xx,y_l(xx))
plt.show()

rho = np.random.randn()

before = sp.limit(rho*y,x,5,dir ="+-")
after = rho*sp.limit(y,x,5,dir ="+-")

print(float(before),float(after))



