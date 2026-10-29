import scipy as spi
import numpy as np

x = np.linspace(0, 1, 100)
f = np.exp(-x**2)-x**2
int1_net = spi.integrate.simpson(f, x)
int1_total = spi.integrate.simpson(np.abs(f), x)


print(int1_net)
print(int1_total)