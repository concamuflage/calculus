
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

x = sp.Symbol('x',real=True)
y = x**2+sp.cos(2*sp.pi*x)/5
y_num = sp.lambdify(x,y,'numpy')

delta = 0.0833
breakpoints =np.arange(0,1,delta)

area = 0
for i in range(len(breakpoints)-1):
    left = breakpoints[i]
    right = breakpoints[i+1]
    mid =(left+right)/2
    height = y.subs(x,mid)
    plt.bar(left,height,width=delta,align='edge',color = 'gray',alpha=0.5)
    area += height*delta

xx = np.linspace(-0.1,1.1,100)
plt.plot(xx,y_num(xx))
plt.show()
print(float(area))