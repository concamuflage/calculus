import sympy as sp
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from IPython.display import Math

x = sp.Symbol('x')
f = sp.cos(x**2)**2+sp.pi

display(Math('f(x)=%s' % sym.latex(f)))
display(Math('f(1)=%s' % sym.latex(f.subs(x,1))))

left = float(sym.limit(f,x,1,dir='-'))
right = float(sym.limit(f,x,1,dir='+'))
two_sided = float(sym.limit(f,x,1))
y = float(f.subs(x,1))

print(left)
print(right)
print(two_sided)
print(y)