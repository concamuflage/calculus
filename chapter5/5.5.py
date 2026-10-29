import sympy as sp

x,a,b,c = sp.symbols("x alpha beta gamma")
f = a*x**2+b*sp.cos(x)
fd = sp.diff(f,x)

f2 = x**2
f2d = sp.diff(f2,x)
f3 = sp.cos(x)
f3d = sp.diff(f3,x)

fd2 = a*f2d+b*f3d



