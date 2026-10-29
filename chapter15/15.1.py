import sympy as sp

x = sp.Symbol("x")

a = 1/x**2
b = sp.pi/x**3
c = 1/sp.sqrt(x)
d = sp.Abs(sp.cos(x))
e = sp.cos(x)
f = sp.cos(x**2)

int_a = sp.integrate(a,(x,1,sp.oo))
int_b = sp.integrate(b,(x,1,sp.oo))
int_c = sp.integrate(c,(x,1,sp.oo))
int_d = sp.integrate(d,(x,0,sp.oo))
int_e = sp.integrate(e,(x,0,sp.oo))
int_f = sp.integrate(f,(x,0,sp.oo))

print(int_a)
print(int_b)
print(int_c)
print(int_d)
print(int_e)
print(int_f)

