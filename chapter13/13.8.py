import sympy as sp

x = sp.Symbol('x',real=True)
f = sp.cos(x)
g = sp.Abs(sp.cos(x))

a = sp.pi/2
b = 5*a
net_area = float(sp.integrate(f,(x,a,b)))
total_area = float(sp.integrate(g,(x,a,b)))
print(net_area)
print(total_area)

solutions = sp.solve(g)
solution = solutions[1]

first = sp.integrate(f,(x,a,solution))
second = sp.integrate(f,(x,solution,b))
total_area_2 = float(sp.Abs(first)+sp.Abs(second))

print(total_area_2)


