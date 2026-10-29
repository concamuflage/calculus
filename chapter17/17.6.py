import numpy as np
from matplotlib import pyplot as plt

t = np.linspace(-2*np.pi, 2*np.pi, 100)
x = np.sin(2*t)+np.sin(t)
y = 2*np.sin(3*t)

plt.scatter(x,y,)
plt.show()

