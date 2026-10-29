import sympy as sp

def myfunc(f,f_d, a,s):

    f_d_s = f_d.subs(x,s)
    f_a = f_d_s*(a-s)+f.subs(x,s)
    return f_a

x = sp.Symbol('x')
f = sp.sqrt(x) + 2*x
f_d = sp.diff(f,x)

approx_function = myfunc(f,f_d,4.37,4)
print(myfunc(f,f_d,4.37,4))
print(f.subs(x,4.37))

