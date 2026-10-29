import numpy as np
import sympy as sp
from IPython.display import display, Math

x = sp.symbols('x', real=True)

def solveMVT(f, a, c):
    """Return points where the Mean Value Theorem slope is attained.

    For example, ``solveMVT(2*x**2 - 3*x + 1, -1, 2)`` returns
    ``array([0.5])``.
    """
    # Use the symbol contained in f, such as x in f = 2*x**2 - 3*x + 1.
    x = next(iter(f.free_symbols))
    df = sp.diff(f, x)
    f_a = f.subs(x, a)
    f_c = f.subs(x, c)
    exp = (f_c - f_a) / (c - a)
    display(Math(r'\frac{f(c)-f(a)}{c-a} = %s' % sp.latex(exp)))
    solutions = sp.solve(df - float(exp))
    b = np.array(solutions).astype(np.float64)
    return b[np.bitwise_and(a < b, b < c)]


if __name__ == '__main__':
    fx = 2 * x**2 - 3 * x + 1

    result = solveMVT(fx, -1, 2)
    print(result)
