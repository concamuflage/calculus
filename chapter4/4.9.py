import sympy as sp
import numpy as np

x = sp.Symbol('x')
piece1 = sp.sin(sp.pi*x)
piece2 = 1.5
piece3 = -(x-2)**2

f = sp.Piecewise(
    (piece1,x<0),
    (piece2,sp.Eq(x,0)),
    (piece3,x>0)
)

sp.plot(f,(x,-1,2))

# all these limits are wrong!
left = sp.limit(f,x,0,dir="-")
right = sp.limit(f,x,0,dir="+")
both = sp.limit(f,x,0,dir="+-")

left = float(left)
right = float(right)
both = float(both)

print(left)
print(right)
print(both)

eps = np.finfo(float).eps
just_left = f.subs(x,0-eps)
just_right = f.subs(x,0+eps)
just_left = float(just_left)
just_right = float(just_right)

# these are closer to the real limit
print(just_left)
print(just_right)


