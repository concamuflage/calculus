
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from section_8_2 import MVTandPlot
from section_8_1 import x

if __name__ == '__main__':
    a = -np.pi/2
    c = 6*np.pi/7
    f = sp.cos(x ** 2)
    fxd = sp.diff(f, x)

    # sp.plot(f)
    # sp.plot(fxd)

    fx_num = sp.lambdify(x, f, 'numpy')
    fxd_num = sp.lambdify(x, fxd, 'numpy')

    # calculate the slope
    f_a = f.subs(x,a)
    f_c = f.subs(x,c)

    slope = (f_c -f_a)/(c-a)
    # find point on fxd that are close to slope by a small number

    xx = np.linspace(-3,4,10000)
    f_values = fx_num(xx)
    fxd_values = fxd_num(xx)
    eta = 0.01
    indices = np.where(np.abs(fxd_values - slope) < eta)[0]
    results = xx[indices]

    for r in results:
        if a< r < c:
            tangent = slope*(x-r)+f.subs(x,r)
            tangent_num = sp.lambdify(x, tangent, 'numpy')
            tangent_values = tangent_num(xx)
            plt.plot(xx,tangent_values,"r")

    # plot the tangent line
    secant = slope*(x-a)+f.subs(x,a)
    secant_num = sp.lambdify(x, secant, 'numpy')
    secant_values = secant_num(xx)
    plt.plot(xx,secant_values,"g")
    plt.plot(xx,f_values)

    # plt.plot(xx,fxd_values)
    plt.show()



