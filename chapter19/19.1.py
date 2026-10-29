import sympy as sp
import scipy.integrate as spint
import numpy as np
x,y = sp.symbols('x,y')

f = sp.exp(sp.pi)*x**2+x*sp.cos(y)-y*sp.exp(sp.pi)*sp.log(x**4)
g = sp.exp(sp.pi)*(x**2+x*sp.cos(y)/sp.exp(sp.pi)-y*sp.log(x**4))
h = (x**2+x*sp.cos(y)/sp.exp(sp.pi)-y*sp.log(x**4))

from IPython.display import display, Math

# display(Math(r'f(x,y) = ' + sp.latex(f)))
# display(Math(r'g(x,y) = ' + sp.latex(g)))

result1 = sp.integrate(f,x,y)
result2 = sp.integrate(sp.exp(sp.pi)*sp.integrate(h,x),y)
result3 = sp.exp(sp.pi)*sp.integrate(h,x,y)

display(Math(r'\mathrm{result1} = ' + sp.latex(result1)))
display(Math(r'\mathrm{result2} = ' + sp.latex(result2)))
display(Math(r'\mathrm{result3} = ' + sp.latex(result3)))

x_b = 3
x_a = 1
y_b = np.pi/4
y_a = -np.pi
result1_def = sp.integrate(f,(x,x_a,x_b),(y,y_a,y_b))
result2_def = sp.integrate(sp.exp(sp.pi)*sp.integrate(h,(x,x_a,x_b)),(y,y_a,y_b))
result3_def = sp.exp(sp.pi)*sp.integrate(h,(x,x_a,x_b),(y,y_a,y_b))

print(float(result1_def))
print(float(result2_def))
print(float(result3_def))

xx = np.linspace(x_a,x_b,100)
yy = np.linspace(y_a,y_b,100)

f_num = sp.lambdify((x,y),f,'numpy')
g_num = sp.lambdify((x,y),g,'numpy')
h_num = sp.lambdify((x,y),h,'numpy')
result4_def = spint.dblquad(
    lambda y, x: f_num(x, y),
    x_a,
    x_b,
    lambda x: y_a,
    lambda x: y_b
)[0]
result5_def = np.exp(np.pi)*spint.dblquad(
    lambda y, x: h_num(x, y),
    x_a,
    x_b,
    lambda x: y_a,
    lambda x: y_b
)[0]
print(result4_def)
print(result5_def)
