import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x',real=True)
f = 3*x**3+2*x - 7*np.pi
df = sp.diff(f, x)

f_num = sp.lambdify(x, f)
xx = np.linspace(-1, 10, 100)

def newton_method(f, df, s, n):

    for num in range(n):

        x4legend = f'{sp.N(s):.3f}'

        color = np.ones(3)*(num/(n-1))
        plt.plot(s, f.subs(x, s), "ko",
                 markerfacecolor=color,
                 markersize=np.max([2, 12 - num*2]),
                 label=r'$x_{%g}=%s$' % (num, x4legend))

        f_s = f.subs(x, s)
        df_s = df.subs(x, s)
        print("iteration", num)
        print("x =", s)
        print("f value =", f_s)
        print("df value =", df_s)
        second = f_s / df_s
        print("second term =", second)

        s = s - second

        print("result =", s)
        print()


    return s

newton_method(f,df,10,4)

plt.plot(xx, f_num(xx))
plt.legend()
plt.show()




