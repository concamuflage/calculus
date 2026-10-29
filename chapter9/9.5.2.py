

# I wanted to add 0.1 to the derivative to avoid the division by zero problem


import sympy as sp

x = sp.Symbol("x")

f = x**3 - 3*x + 3
df = sp.diff(f, x)


def modified_newton(f, df, s, n, epsilon):
    print(f"\nepsilon = {epsilon}")

    for i in range(n):
        f_s = float(f.subs(x, s))
        df_s = float(df.subs(x, s))

        print(
            f"iteration {i}: "
            f"x = {s:.10f}, "
            f"f(x) = {f_s:.10f}, "
            f"f'(x) = {df_s:.10f}"
        )

        # Your proposed solution
        s = s - f_s / (df_s + epsilon)

    return s

for epsilon in [0.1, 0.01, 0.001]:
    result = modified_newton(f, df, 0.0, 5, epsilon)
    print("final =", result)
    print("final_y",f.subs(x,result))
