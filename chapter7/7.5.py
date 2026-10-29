import sympy as sp

from IPython.display import display, Math

x, y = sp.symbols("x y")

eq = sp.Eq(x**3*y**2 - 5*x**4, 0)

y_explicit = sp.solve(eq, y)

for solution in y_explicit:

    display(Math(r'y = %s' % sp.latex(solution)))

d1 = sp.idiff(eq.lhs,y,x)
d2 = sp.diff(y_explicit[0],x)
d3 = sp.diff(y_explicit[1],x)

display(Math(r'\frac{dy}{dx} = %s' % sp.latex(d1)))

display(Math(r'\frac{dy_1}{dx} = %s' % sp.latex(d2)))

display(Math(r'\frac{dy_2}{dx} = %s' % sp.latex(d3)))


