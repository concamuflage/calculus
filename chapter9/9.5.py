import sympy as sp


# given a function and a starting point
#  the derivative can land on 0 after some iterations.
def newton_method(f, df, s, n):

    for num in range(n):
        f_s = f.subs(x, s)
        df_s = df.subs(x, s)

        print("iteration", num)
        print("x =", s)
        print("f value =", f_s)
        print("df value =", df_s)

        if df_s == 0:
            print("STOP: derivative is 0")
            break

        second = f_s / df_s
        print("second term =", second)

        s = s - second
        print("result =", s)
        print()

    return s


x = sp.Symbol('x', real=True)

f = x**3 - 3*x + 3
df = sp.diff(f, x)

result = newton_method(f, df, 0, 10)

print("final:", result)