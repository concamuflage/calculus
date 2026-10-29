import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x',real=True)

f = x**2-2*x
a = -0.5
bs = np.linspace(0,3.5,30)
total_areas = []
net_areas = []

for b in bs:
    result_net = sp.integrate(f, (x, a, b))
    result_total = sp.integrate(sp.Abs(f),(x,a,b))

    total_areas.append(result_total)
    net_areas.append(result_net)
total_areas = np.array(total_areas)
net_areas = np.array(net_areas)

sp.plot(f)
plt.plot(bs,total_areas,color='red')
plt.plot(bs,net_areas,color="green")
plt.show()

anti1 = sp.Integral(f,x)
anti2 = sp.Integral(sp.Abs(f),x)
from IPython.display import display, Math
display(Math(r'\int f(x)\,dx = ' + sp.latex(anti1) + r' + C'))
display(Math(r'\int |f(x)|\,dx = ' + sp.latex(anti2) + r' + C'))

g= sp.cos(2*sp.pi*x)
anti3 = sp.integrate(g,x)

print(anti3)
