import sympy as sp

x = sp.Symbol("x")

f = 3*x**2
g = x**3+sp.log(x)
h = sp.cos(x)

f_g_x = f.subs(x,g)

result1 = sp.diff(f_g_x,x)

g_d = sp.diff(g,x)
f_g_d = sp.diff(f_g_x,g)
result2 = f_g_d*g_d


