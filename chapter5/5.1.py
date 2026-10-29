import numpy as np
import matplotlib.pyplot as plt
from zmq.backend import first

_,axs = plt.subplots(1,2)
n = 1000
x = np.linspace(-1,5,n)
y = x**2
axs[0].plot(x,y,"o-")

delta_x = (x[1]-x[0])
slopes = np.diff(y)/1

for i in range(0,n-1):
    first_point = [x[i],slopes[i]]
    second_point = [x[i+1],slopes[i]]
    axs[1].plot(
        [x[i],x[i+1]],
        [slopes[i],slopes[i]],
        "o-"
    )

plt.show()




