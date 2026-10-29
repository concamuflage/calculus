import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x',real=True)
f = 3*x**3+2*x - 7*np.pi
df = sp.diff(f, x)

n = 6
iterations = np.arange(0,6)
def newton_method(f, df, s, n):

    estimates = []
    estimates.append(s)
    for num in range(n):
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
        estimates.append(s)


    return estimates


estimates = newton_method(f,df,1,n-1)
print(iterations)
print(estimates)
plt.plot(iterations,estimates,"s-")
plt.axhline(y=1.8,color="r")
plt.show()


