import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def myfunc(f,f_d, a,s):

    f_d_s = f_d.subs(x,s)
    f_a = f_d_s*(a-s)+f.subs(x,s)
    return f_a

x = sp.Symbol('x',real = True)
results_approx = []
results_real = []
f = sp.Abs(sp.sin(x))
f_d = sp.diff(f,x)

sp.plot(f)
sp.plot(f_d,detect_poles=True)

result = myfunc(f,f_d,(5*sp.pi)/8,sp.pi/2)

print(result)

xx = np.linspace(-np.pi ,2*np.pi,100)

result_list = []
for num in xx:
    r = myfunc(f,f_d,(5*sp.pi)/8,num)
    result_list.append(r)

result_list = np.array(result_list)
errors = result_list - 1

plt.plot(xx,errors,"o")
plt.show()


