import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
_,axes = plt.subplots(1,3)

x = sp.Symbol('x',real=True)

f = sp.exp(-x)*sp.cos(2*sp.pi*x)
g = x**3-1
h = sp.exp(-sp.Abs(x))

a = -0.5
b = 1
n = 10

f_num = sp.lambdify(x,f,'numpy')
g_num = sp.lambdify(x,g,'numpy')
h_num = sp.lambdify(x,h,'numpy')


xx = np.linspace(-1,1.5,10)
funcs = [f_num,g_num,h_num]
for i in range(3):
    axes[i].plot(xx,funcs[i](xx))
    axes[i].axhline(0)
    axes[i].fill_between(xx,0,funcs[i](xx),where = (xx>a) & (xx<b), color = "gray",alpha = 0.5)

# net area
integral_0 = sp.integrate(f,(x,a,b))
integral_1 = sp.integrate(g,(x,a,b))
integral_2 = sp.integrate(h,(x,a,b))

# total area

integral_0_total = sp.integrate(sp.Abs(f),(x,a,b))
integral_1_total = sp.integrate(sp.Abs(g),(x,a,b))
integral_2_total = sp.integrate(sp.Abs(h),(x,a,b))

print("net area")
print(float(integral_0))
print(float(integral_1))
print(float(integral_2))

print("total area")
print(float(integral_0_total))
print(float(integral_1_total))
print(float(integral_2_total))
plt.show()




