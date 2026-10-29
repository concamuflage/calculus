import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy.polys.benchmarks.bench_solvers import F_abc

x = sp.Symbol('x')
powers = np.linspace(-3,1,21)

_,axes = plt.subplots(1,2)
bool = np.empty(21)
xx = np.linspace(1,10,100)
for i, p in enumerate(powers):
    f = x**p
    F= sp.integrate(f, x)
    F_a = sp.limit(F,x,sp.oo)
    F_b = F.subs(x,1)
    fin_int = F_a - F_b
    c = 'k' if fin_int.is_finite else [.6, .8, .6]
    if fin_int.is_finite:
        bool[i] = 0
    else:
        bool[i] = 1

    F_num = sp.lambdify(x,F,'numpy')
    axes[0].plot(xx,F_num(xx),color = c)

axes[0].set_ylim(-10,30)
axes[1].plot(powers, bool, 'x')
axes[1].set_ylim(-1,2)
plt.show()


