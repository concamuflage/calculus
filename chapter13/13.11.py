import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

n = 1000
x = sp.Symbol('x',real=True)
y = x**2+sp.cos(2*sp.pi*x)/5
y_num = sp.lambdify(x,y,'numpy')

xx = np.linspace(0,1,n+1)
aa = y_num(xx)

# find the index of xx that has max y and min y

index_max = np.argmax(aa)
index_min = np.argmin(aa)

y_max = aa[index_max]
y_min = aa[index_min]

yy = np.linspace(y_min,y_max,n+1)

# use a dictionary to find all x such that y = f(x) for a given y

dict = {}
for i,num in enumerate(xx):
    rounded = round(aa[i],5)
    if rounded in dict:
        dict[rounded].append(num)
    else:
        dict[rounded] = [num]

for y_val in dict:
    xs = dict[y_val]
    plt.hlines(y_val, 0,min(xs))
    if len(dict[y_val]) > 1:
        plt.hlines(y_val,max(xs),1)

plt.show()






