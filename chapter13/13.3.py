
import matplotlib.pyplot as plt
import numpy as np
from numpy.ma.core import left_shift
import sympy as sp

# break points
a = -0.5
b = np.pi
n = 10000
delta = (b-a) / n
break_1 = [ a + x* delta for x in range(n+1)]
break_2 = np.linspace(a,b,n+1)

_,axes = plt.subplots(3,1)
# function
xx = np.linspace(-1,4,100)

def f(x):
    return np.exp(x)/10 +np.cos(x)

for i in range(3):
    for bb in break_1:
        axes[i].plot([bb, bb], [0, 0.05], color='black')
    shaded_indices = (xx > a) & (xx < b)
    shaded_xx = xx[shaded_indices]
    shaded_yy = f(shaded_xx)
    axes[i].fill_between(shaded_xx, shaded_yy, color='gray')
    axes[i].plot(xx, f(xx))
    axes[i].set_xticks([-1, 0, 1, 2, 3])
    axes[i].set_xlim([-1, 3.5])
    axes[i].set_ylim([0, 2])
    axes[i].vlines(a, 0, f(a))
    axes[i].vlines(b, 0, f(b))

# left_rule

area_left = 0
for i in range(len(break_1)-1):
    left = break_1[i]
    height = f(left)
    width = delta
    axes[0].bar(left,height,width,align='edge',alpha=0.3,facecolor='none',edgecolor='black')
    area_left += height * delta

# right rule
area_right = 0
for i in range(len(break_1)-1):
    left = break_1[i]
    right = break_1[i+1]
    height = f(right)
    width = delta
    axes[1].bar(left,height,width,align='edge',alpha=0.3,facecolor='none',edgecolor='black')
    area_right += height * delta

# mid rule

area_mid = 0
for i in range(len(break_1)-1):
    left = break_1[i]
    right = break_1[i+1]
    height = (f(right)+f(left))/2
    width = delta
    axes[2].bar(left,height,width,align='edge',alpha=0.3,facecolor='none',edgecolor='black')
    area_mid += height * delta

# mid_point rule
plt.show()

x = sp.Symbol('x',real=True)
f = sp.exp(x)/10 +sp.cos(x)
ground_truth = sp.integrate(f,(x,a,b))

print(area_left)
print(area_right)
print(area_mid)
print(ground_truth)

