import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.Symbol('x',real=True)
f = x**2-0.5

f_num = sp.lambdify(x,f,'numpy')
dx = 0.2
xx = np.arange(-0.5,1+dx,dx)
print(xx)
left = xx - 0.1
right = xx + 0.1

# aa = np.unique(
#     np.round(np.concatenate((left, right)), 10)
# )
# print(aa)
plt.plot(xx,f_num(xx))
plt.plot(xx,f_num(xx),"ks")
plt.axhline(y=0,color="r")

# approach 1
# for i in range(len(aa)-1):
#     left_edge = aa[i]
#     right_edge = aa[i+1]
#     width = 0.2
#     mid_point = (left_edge + right_edge)/2
#     height = f_num(mid_point)
#     plt.bar( left_edge, height,width,align='edge')

# approach 2,without need for aa
area = 0
for mid in xx:
    left = mid -dx/2
    right = mid + dx/2
    height = float(f.subs(x,mid))
    plt.fill_between([left,right],[height,height],edgecolor='k',facecolor=[.9,.9,.9])
    area += np.abs(height*dx)

plt.show()
print(area)