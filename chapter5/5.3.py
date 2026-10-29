import numpy as np
import matplotlib.pyplot as plt

n = 100
x = np.linspace(-1,1,n)
y = x**3-x**2

y_prime_analytical = 3*x**2-2*x
y_prime_empirical = np.diff(y)/(x[1]-x[0])

_,axes = plt.subplots(1,3)

axes[0].plot(x,y,"o-")
axes[1].plot(x,y_prime_analytical,"o-")
axes[1].plot(x[:-1],y_prime_empirical,"o-")


# calculate root mean squared

rms_list = []
index = np.arange(10,n)
for n in range(10,n):
    x = np.linspace(-1, 1, n)
    y = x ** 3 - x ** 2
    y_prime_analytical = 3 * x ** 2 - 2 * x
    y_prime_empirical = np.diff(y) / (x[1] - x[0])
    rms = np.sqrt(np.mean((y_prime_analytical[:-1]-y_prime_empirical)**2))
    rms_list.append(rms)

axes[2].plot(index,rms_list,"o-")

plt.show()