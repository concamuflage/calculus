import sympy as sp

x = sp.Symbol('x',real=True)
f = sp.Abs(sp.cos(x))
fd = sp.diff(f,x)

sp.plot(f)
sp.plot(fd)
