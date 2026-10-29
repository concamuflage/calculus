import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

_,axes = plt.subplots(1,3)
xx = np.linspace(-1,4,27)
delta_x = xx[1] - xx[0]
x = sp.Symbol('x')

f = x**2

f_num = sp.lambdify(x,f,'numpy')
f_values = f_num(xx)
df_values = np.diff(f_values)/delta_x

df_values = np.append(df_values,df_values[-1])

# integrals


index = np.argmin(np.abs(xx))


idf = np.cumsum(df_values * delta_x)
close_to_zero = idf[index]
idf = idf - close_to_zero

f_0_value = float(f.subs(x,0))
idf = idf + f_0_value


axes[0].plot(xx,f_values,"s")
axes[1].plot(xx,df_values,"s")
axes[2].plot(xx, idf, "s")
plt.show()

# print the table
# header row
print('  x    |   fx    |   df    |   idf')
print('-----------------------------------')
# now for the results
for i in range(len(xx)):
  print(f'{xx[i]:>5.2f}  |  {f_values[i]:>5.2f}  |  {df_values[i]:>5.2f}  |  {idf[i]:>5.2f}')









