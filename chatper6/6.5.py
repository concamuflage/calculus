from logging import critical

import numpy as np
import sympy
import sympy as sp
import matplotlib.pyplot as plt

xx = np.linspace(-5,7,20)
aa = np.linspace(-1,3,22)
x = sp.Symbol('x')
fig, axs = plt.subplots(2,1)
for a in aa:
    fx = (2 * (x - a) ** 2 + 3) / ((x - 1) ** 2 + 2)
    df = sp.diff(fx, x)
    dff = sp.diff(fx, x,2)
    fx_num = sp.lambdify(x,fx)
    fx_prime_num = sp.lambdify(x, df)
    fx_values = fx_num(xx)
    fx_prime_values = fx_prime_num(xx)

    # find critical points
    critical = sp.solveset(df, x, domain=sp.S.Reals)
    critical = list(critical)
    # find the maximum

    critical_values = [float(fx.subs(x,c)) for c in critical]

    # index = np.argmax(critical_values)
    # max = critical[index]
    # axs[0].plot(max,fx.subs(x,max) , "o")

    for c in critical:
        if float(dff.subs(x,c)) < 0:
            y = float(fx.subs(x,c))
            axs[0].plot(c, y,"o")

    axs[0].plot(xx,fx_values)
    axs[1].plot(xx,fx_prime_values)

plt.show()





