import numpy as np
import matplotlib.pyplot as plt
import scipy as sip

from chapter17.simulation import segLengths
_,axes = plt.subplots(1,2)

deltas  = [1,0.001]
colors  = ['red','green']
for i, delta in enumerate(deltas):
    t = np.arange(0, 12 * np.pi, delta)
    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5)
    x_diff = x[1:] - x[:-1]
    y_diff = y[1:] - y[:-1]
    segLengths = np.sqrt(x_diff ** 2 + y_diff ** 2)
    length1 = np.sum(segLengths)
    # calculating length with the formula
    dxdt = x_diff/delta
    dydt = y_diff/delta
    integrand = np.sqrt(dxdt**2 + dydt**2)
    length2 = sip.integrate.simpson(integrand, t[1:])
    axes[0].scatter(x, y,color = colors[i],s = 10,alpha = 0.3,zorder=2-i)
    print(length1, length2)

deltas  = np.linspace(1,0.0001,31)

simple_lengths = []
simpson_lengths = []
for i, delta in enumerate(deltas):
    t = np.arange(0, 12 * np.pi, delta)
    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5)
    x_diff = x[1:] - x[:-1]
    y_diff = y[1:] - y[:-1]
    segLengths = np.sqrt(x_diff ** 2 + y_diff ** 2)
    length1 = np.sum(segLengths)
    # calculating length with the formula
    dxdt = x_diff/delta
    dydt = y_diff/delta
    integrand = np.sqrt(dxdt**2 + dydt**2)
    length2 = sip.integrate.simpson(integrand, t[1:])
    simple_lengths.append(length1)
    simpson_lengths.append(length2)

axes[1].plot(deltas, simple_lengths,"rs")
axes[1].plot(deltas, simpson_lengths,"gs")

plt.show()
