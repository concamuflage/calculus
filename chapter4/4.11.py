import sympy as sp

location =0
x = sp.Symbol('x')

f1 = (sp.cos(x)-1)/x
f2 = sp.sin(x)/x
f3 = x**2*sp.sin(1/x)
f4 = sp.sin(x)/x
f5 = sp.tan(x)/x

limit1 = sp.limit(f1,x,location,dir="+-")
limit2 = sp.limit(f2,x,location,dir="+-")
limit3 = sp.limit(f3,x,location,dir="+-")
limit4 = sp.limit(f4,x,sp.oo,dir="+-")
limit5 = sp.limit(f5,x,location,dir="+-")

limit1 = float(limit1)
limit2 = float(limit2)
limit3 = float(limit3)
limit4 = float(limit4)
limit5 = float(limit5)

print(limit1,limit2,limit3,limit4,limit5)
