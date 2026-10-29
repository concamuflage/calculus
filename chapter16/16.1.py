import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import scipy as sip

xx = np.linspace(-2*np.pi,3*np.pi,803)
f = np.cos(xx)*xx
areas = sip.integrate.cumulative_trapezoid(f,xx,initial=0)
plt.plot(f,areas)
plt.show()