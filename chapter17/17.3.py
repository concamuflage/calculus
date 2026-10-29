import sympy as sp
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

x = sp.Symbol('lamda',real=True)
f = sp.sqrt(sp.Abs(x))+3
g = x**2+sp.E/2
h = sp.Abs(x)**sp.E

# try to find intersection analytically

# eq1 = sp.Eq(f,g)
# eq2 = sp.Eq(g,h)
# solutions = sp.solve(eq1,x)
# solutions2 = sp.solve(eq2,x)
#
# print(solutions)
# print(solutions2)

# find the intersection numerically

xx = np.linspace(-5,5,10000)
delta = xx[1] - xx[0]
f_num = sp.lambdify(x,f,'numpy')
g_num = sp.lambdify(x,g,'numpy')
h_num = sp.lambdify(x,h,'numpy')
f_val = f_num(xx)
g_val = g_num(xx)
h_val = h_num(xx)

diff_fg = np.abs(f_val - g_val)
diff_gh = np.abs(h_val - g_val)
deri_diff_fg = np.diff(diff_fg)/delta
deri_diff_gh = np.diff(diff_gh)/delta

error_fg= 0.0015
error_gh= 0.001
indices_fg = np.where(diff_fg < error_fg)[0]
indices_gh = np.where(diff_gh < error_gh)[0]
solutions_fg = diff_fg[indices_fg]
solutions_gh = diff_gh[indices_gh]
final_index_fg = []
final_index_gh = []
for num in indices_fg:
    if (deri_diff_fg[num-1]<0 and deri_diff_fg[num+1] > 0):
        final_index_fg.append(num)

for num in indices_gh:
    if (deri_diff_gh[num-1]<0 and deri_diff_gh[num+1] > 0):
        final_index_gh.append(num)

final_solutions_fg = xx[final_index_fg]
final_solutions_gh = xx[final_index_gh]
print(final_solutions_fg)
print(final_solutions_gh)

# calculate areas
area1 = sp.integrate(f-g,(x,final_solutions_fg[0],final_solutions_gh[1]))
area2 = sp.integrate(g-h,(x,final_solutions_gh[0],final_solutions_gh[1]))
print(float(area1))
print(float(area2))
plt.show()



