import sympy as sp

x = sp.Symbol('x')
C = sp.Symbol('C')
fd = x**(sp.Rational(5,2))+ sp.cos(x)
f = sp.integrate(fd, x) + C

# solve for C

solutions = sp.solve(f.subs(x,1)-sp.pi,C)
print(float(solutions[0]))

print(f)