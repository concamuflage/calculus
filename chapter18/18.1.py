import numpy as np
import scipy as sip

import matplotlib.pyplot as plt

xx = np.linspace(-4,4,100)
sigma = 0.5
yy = 1/np.sqrt(2*np.pi*sigma**2)*np.exp(-xx**2/(2*sigma**2))
delta_x = xx[1]-xx[0]

cdf1 = np.cumsum(yy*delta_x)
cdf2 = sip.integrate.cumulative_trapezoid(yy,xx,initial=0)
cdf3 = sip.integrate.cumulative_simpson(yy,x=xx,initial=0)
cdf4 = sip.stats.norm.cdf(xx,loc=0,scale=sigma)

plt.plot(xx,cdf1,"r")
plt.plot(xx,cdf2,"g")
plt.plot(xx,cdf3,"b")
plt.plot(xx,cdf4,"k")
plt.show()
