import sympy as sp
import scipy.signal as signal
import numpy as np

x = sp.Symbol('x')
f = sp.log(x)
df = sp.diff(f,x)

eq = sp.Eq(f,df)
solutions = sp.solve(eq,x)
print(float(solutions[0]))

# calculate numerically
xx = np.linspace(0.0001,5,1000)
f_num = sp.lambdify(x,f)
df_num = sp.lambdify(x,df)
f_vals = f_num(xx)
df_vals = df_num(xx)
diff = f_vals - df_vals
peaks_indices = signal.find_peaks(-np.abs(diff))[0]

print(peaks_indices)

final_index = []
for index in peaks_indices:
    if diff[index-1]*diff[index+1] >0:
        final_index.append(index)
intersections = xx[final_index]
print(intersections)











