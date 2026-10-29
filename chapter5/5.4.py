import sympy as sp
import numpy as np
from sklearn.covariance import empirical_covariance

x = sp.Symbol('x')

f1 = (sp.sympify(5)/4)*x+sp.sympify(9)/4
f2 = x**3-x**2
f3 = sp.sqrt(x)+sp.cos(x)
f4 = sp.exp(x)

f1d = sp.diff(f1,x)
f2d = sp.diff(f2,x)
f3d = sp.diff(f3,x)
f4d = sp.diff(f4,x)

vals = [-1,0,2]
f4d_fun = sp.lambdify(x,f4d)
for val in vals:
    analytic_derivative = f4d.subs(x,val)
    empirical_derivative = f4d_fun(val)
    print(val, analytic_derivative, empirical_derivative)







