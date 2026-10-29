import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def myfunc(f,f_d, a,s):

    f_d_s = f_d.subs(x,s)
    f_a = f_d_s*(a-s)+f.subs(x,s)
    return f_a

x = sp.Symbol('x')
f = sp.sqrt(x) + 2*x
f_d = sp.diff(f,x)

results_approx = []
results_real = []
xx = np.arange(5,14)
for num in range(5,14):
    result = myfunc(f,f_d,num,10)
    results_approx.append(result)
    results_real.append(f.subs(x,num))

differences = np.abs(np.array(results_approx) - np.array(results_real))

plt.plot(xx,differences)
plt.show()


