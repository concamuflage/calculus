import sympy as sp

x = sp.symbols('x')
f = sp.exp(-x**2)
g = x**2
h = f-g

F = sp.integrate(f,x)
G = sp.integrate(g,x)
H = sp.integrate(h,x)

area1 = H.subs(x,1) - H.subs(x,0)
area2 = (F.subs(x,1) - F.subs(x,0))-(G.subs(x,1) - G.subs(x,0))

print(area1)
print(area2)