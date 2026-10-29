import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,4*np.pi/5,123)
x = np.cos(2*t)
y = np.sin(t**2)
colors = np.linspace([0.8,0.8,0.8],[0,0,0],123)

_,axes = plt.subplots(1,3)
segLengths = np.zeros(len(t))

for i in range(1,len(t)):
    dx = x[i]-x[i-1]
    dy = y[i]-y[i-1]
    segLengths[i] = np.sqrt(dx**2+dy**2)



# 1
axes[0].scatter(x,y,10,c = colors)
axes[1].scatter(t,segLengths,10,c = colors)
axes[2].scatter(t,np.cumsum(segLengths),10,c = colors)








