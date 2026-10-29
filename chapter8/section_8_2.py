import numpy as np
import sympy as sp

from section_8_1 import solveMVT,x
from matplotlib import pyplot as plt

def MVTandPlot(f, a, c):
    """Plot a function with its MVT tangent and secant lines.

    For example, ``MVTandPlot(2*x**2 - 3*x + 1, -1, 2)`` displays the
    quadratic, the secant through the endpoints, and a parallel tangent.
    """
    # Use the symbol contained in f so this function works when imported.
    x = next(iter(f.free_symbols))
    f_a = f.subs(x, a)
    f_c = f.subs(x, c)
    slope = (f_c - f_a) / (c - a)
    secant = slope * (x - a) + f_a
    f_num = sp.lambdify(x, f, 'numpy')
    secant_num = sp.lambdify(x, secant, 'numpy')

    multiple_b = solveMVT(f, a, c)
    n = 4
    xx = np.linspace(-n, n, 100)

    # handle multiple tangent lines
    for b in multiple_b:
        f_b = f.subs(x, b)
        tangent = slope * (x - b) + f_b
        tangent_num = sp.lambdify(x, tangent, 'numpy')
        plt.plot(xx, tangent_num(xx), "r")

    plt.plot(xx, f_num(xx))
    plt.plot(xx, secant_num(xx), "g")
    plt.plot(a, f_a, "ko")
    plt.plot(c, f_c, "ko")
    plt.show()


if __name__ == '__main__':
    fx = 2 * x**2 - 3 * x + 1
    MVTandPlot(fx, -1, 2)

