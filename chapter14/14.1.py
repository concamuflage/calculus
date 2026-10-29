import numpy as np
import sympy as sp
from IPython.display import display, Math
import matplotlib.pyplot as plt

x = sp.Symbol('zeta')

for num in range(1,7):
    f = x**(sp.Rational(num,2))
    f_integral = sp.integrate(f,x)

    display(Math(

        sp.latex(sp.Integral(f, x))

        + " = "

        + sp.latex(f_integral)

        + " + C"

    ))

    f_num = sp.lambdify(x, f)
    f_integral_num = sp.lambdify(x, f_integral)

    xx = np.linspace(0,1.4,100)
    plt.plot(xx,f_integral_num(xx),color='black',linestyle = '--')
    plt.plot(xx,f_num(xx),color='blue')
    plt.plot(xx,f_num(xx))

plt.show()
