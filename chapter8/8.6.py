import numpy as np
import sympy as sp

a = np.pi/2
c = (3*np.pi)/2
x = sp.Symbol('x',real=True)
f = sp.Abs(sp.sin(x))
f_d = sp.diff(f)

sp.plot(f,(x,a,c))
sp.plot(f_d,(x,a,c))


solutions = sp.solve(f_d, x)[0]
solution = np.array(solutions)
real = solution[(solution<c) & (solution > a )]

print(solutions)