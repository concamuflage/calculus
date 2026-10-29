import sympy as sp

x = sp.Symbol('x')

f = x**3-3*x;

df = sp.diff(f,x);
dff = sp.diff(f,x,2);

critical_points = sp.solve(df,x);
print(critical_points)
inflection_points = sp.solve(dff,x);
print(inflection_points)

print(df);
print(dff);

# for visualizing the functions