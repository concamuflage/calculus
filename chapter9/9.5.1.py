import sympy as sp
from sklearn.metrics import f1_score

# in the first iteration, derivative goes to 0 , causing
# a division by zero problem
# we could make s= 0.000001

def newton_method(f,df, s,n):

    for num in range(n):
        f_s = f.subs(x,s)
        df_s = df.subs(x,s)
        second = f_s/df_s
        print("iteration",num)
        print("f value",f_s)
        print("df value",df_s)
        print("second term",second)
        s = s - second
        print("result",s)

    return s

x = sp.Symbol('x',real=True)
f = 2*x**3 - 3
df = sp.diff(f,x)
result = sp.solve(f)[0]
print(float(result))

result = newton_method(f,df,0,10)
print(result)
