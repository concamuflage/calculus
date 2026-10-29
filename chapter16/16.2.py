import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import scipy as sip

x = sp.Symbol('x')
y = sp.exp(-sp.pi*x)
z = sp.sin(7*x)
f = y*z

fn = sp.integrate(f,x)
latex = sp.latex(fn)

plt.figure(figsize=(10, 2))

plt.text(0.5, 0.5, f'${latex}$',

         fontsize=20, ha='center', va='center')

plt.axis('off')

plt.show()
