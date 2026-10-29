import sympy as sp

x,y = sp.symbols("x y")
f = 2*x +4/y

limX = sp.limit(f,x,0 )
limY = sp.limit(f,y,2)

print(limX)
print(limY)

limit1 = sp.limit(limX,y,2)
limit2 = sp.limit(limY,x,0)

print(limit1)
print(limit2)
