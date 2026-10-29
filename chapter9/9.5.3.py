
# code for proving that adding 0.1 won't solve the derivative = 0 problem
# the real derivative could be -0.1 and this still makes derivative+0.1 =0

import sympy as sp

x = sp.Symbol("x")

f = x**2 - 1

df = sp.diff(f, x)

# Choose x so that f'(x) = -0.1

s = -0.05

print("f'(x) =", df.subs(x, s))

print("modified denominator =", df.subs(x, s) + 0.1)

result = f.subs(x, s) / (df.subs(x, s) + 0.1)

print(result)