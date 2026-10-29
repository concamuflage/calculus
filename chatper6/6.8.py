import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from sympy import lambdify
from matplotlib import pyplot as plt

x = sp.symbols('x', real=True)

f = sp.log(sp.Abs(x)) + sp.cos(x)
df = sp.diff(f, x)
ddf = sp.diff(df, x)

# Display f(x), f'(x), and f''(x)
fig, ax = plt.subplots(figsize=(10, 4))

equations = (
    rf'$f(x) = {sp.latex(f)}$' + '\n\n'
    + rf"$f'(x) = {sp.latex(df)}$" + '\n\n'
    + rf"$f''(x) = {sp.latex(ddf)}$"
)

ax.text(
    0.5, 0.5,
    equations,
    fontsize=18,
    ha='center',
    va='center'
)

ax.axis('off')
plt.show()


xx = np.linspace(-3*np.pi,3*np.pi,10000)
f_num = lambdify(x,f,'numpy')
df_num = lambdify(x,df,'numpy')
# ddf_num = lambdify(x,ddf,'numpy')
expression = [float(ddf.subs(x,xi)) for xi in xx]
ddf_num = np.array(expression)

f_values = f_num(xx)
df_values = df_num(xx)
expression = [float(ddf.subs(x,xi)) for xi in xx]
ddf_values = np.array(expression)

# to find critical points

critical_candidates = find_peaks(-abs(df_values))[0]
critical_index = []
for c in critical_candidates:
    if df_values[c-1]*df_values[c+1]<0:
        critical_index.append(c)

critical_index = np.array(critical_index)
critical_index = critical_index +1
critical_x = xx[critical_index]
critical_y = f_values[critical_index]
print("critical points:")
for x,y in zip(critical_x,critical_y):
    print(x,y)


# to find inflection points

inflection_candidates = find_peaks(-abs(ddf_values))[0]
inflection_index = []
for c in inflection_candidates:
    if ddf_values[c-1]*ddf_values[c+1]<0:
        inflection_index.append(c)

inflection_index = np.array(inflection_index)
inflection_index = inflection_index +1
inflection_x = xx[inflection_index]
inflection_y = f_values[inflection_index]
print("inflection points:")
for x,y in zip(inflection_x,inflection_y):
    print(x,y)

# must observe the plot and add critical and inflection points

_,axs = plt.subplots(1,3)

axs[0].plot(xx,f_values,'ro')
axs[0].plot(critical_x,critical_y,'ko')
axs[0].plot(inflection_x,inflection_y,'ko')

axs[1].plot(xx,df_values,'ro')
axs[1].plot(critical_x,df_values[critical_index],'ko')
axs[1].set(ylim=[-20,20])
axs[2].plot(xx,ddf_values,'ro')
axs[2].set(ylim=[-20,20])
axs[2].plot(inflection_x,ddf_values[inflection_index],'ko')

plt.show()