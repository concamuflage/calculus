import sympy as sp
from IPython.core.display import Math
from IPython.core.display_functions import display

x = sp.Symbol('x')
y = x**2*sp.log(x)

y_limit = sp.limit(y,x,0,dir="+")

print(y_limit)

f = x**2
g = sp.log(x)
h = f/g

h_d = sp.diff(h,x)

f_d = sp.diff(f,x)
g_d = sp.diff(g,x)
ratio = f_d/g_d

# print h_d
# print ratio

# plot

sp.plot(y)



# Solve h'(x) = 0

solutions = sp.solve(sp.Eq(h_d, 0), x)
display(Math(r"h'(x) = %s" % sp.latex(h_d)))
display(Math(r"h'(x)=0 \Rightarrow x=%s" % sp.latex(solutions)))