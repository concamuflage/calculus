import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Define polar function
theta = sp.symbols('theta')

r = (3 * sp.sin(theta) * sp.cos(theta)) / (
    sp.sin(theta)**3 + sp.cos(theta)**3
)

r_num = sp.lambdify(theta, r, 'numpy')

# Numerical values
tt = np.linspace(0, 2*np.pi, 1000)
r_values = r_num(tt)

# Create figure
fig = plt.figure(figsize=(10, 5))

# First plot: polar
ax1 = fig.add_subplot(1, 2, 1, projection='polar')
ax1.plot(tt, r_values)
ax1.set(rlim=[0,2.5],rticks=[1,2],title=r'$\bf{A}$)  Polar coords')
ax1.set_title('Polar plot')

# Second plot: r versus theta

t = np.linspace(-10, 10, 100)
x = 3*t/(1+t**3)
y =(3*t**2)/(1+t**3)
ax2 = fig.add_subplot(1, 2, 2)
ax2.scatter(x, y)
ax2.set(xlim=[-5,5],ylim=[-5,5],xlabel='x',ylabel='y',title=r'$\bf{B}$)  Rectanguar coords')
plt.show()