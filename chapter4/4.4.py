import sympy as sp

x = sp.Symbol('x')
y = sp.Abs(x-2)/(x-2)

left = sp.limit(y,x,2,dir="-")
right = sp.limit(y,x,2,dir="+")
both = sp.limit(y,x,2,dir="+-")

print(left,right, both)