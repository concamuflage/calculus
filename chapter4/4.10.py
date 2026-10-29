import numpy as np
import sympy as sp

x = sp.Symbol('x')
y = sp.sin(1/x)

n = 1
sp.plot(y,(x,-n,n))

left = sp.limit(y,x,0,dir="-")
right = sp.limit(y,x,0,dir="+")
both = sp.limit(y,x,0,dir="+-")

print(left)
print(right)
print(both)

eps = np.finfo(float).eps
slight_left = y.subs(x,0-eps)
slight_right = y.subs(x,0+eps)
both = y.subs(x,0)


# the following logic is wrong!
# as the function approaches 0, it fluctuates more often.

print("more accurate estimation")
print(slight_left)
print(slight_right)
print(both)


print(y.subs(x,-0.000001))
print(y.subs(x,-0.000002))
print(y.subs(x,-0.000003))


