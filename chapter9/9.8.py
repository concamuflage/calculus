import sympy as sp

x = sp.Symbol('x',real=True)

f = 200*x+60000/x
fd = sp.diff(f,x)
fdd = sp.diff(fd,x)

solutions = sp.solve(fd,x)

for solution in solutions:
    if fdd.subs(x,solution) > 0:
        print(float(solution))


