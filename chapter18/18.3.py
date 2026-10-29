import numpy as np
import sympy as sp
import scipy.stats as stats

import matplotlib.pyplot as plt

xx = np.linspace(0,5,100)
delta = xx[1]-xx[0]
a = 1
b = 3
d = 4

cdf = np.zeros(len(xx))

#piece1

whereX = xx<a
cdf[whereX] = 0
#piece2

whereX = (xx>a) & (xx<b)
cdf[whereX] = (xx[whereX]-a)**2 / ((d-a)*(b-a))
#piece3
whereX = (xx>b) & (xx<d)
cdf[whereX] = 1 - ((d-xx[whereX])**2 / ((d-a)*(d-b)))
#piece4
whereX = xx>d
cdf[whereX] = 1

pdf = np.diff(cdf)/delta

pdf2 = stats.triang.pdf(xx,loc=a,c=(b-a)/(d-a),scale=d-a)*delta

plt.plot(xx,cdf,'r')
plt.plot(xx[1:],pdf,'b')
plt.plot(xx,pdf2,'g')
plt.show()