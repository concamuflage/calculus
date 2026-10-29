import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import scipy as sip

import matplotlib.pyplot as plt
x,y = sp.symbols('x y',real=True)

f = sp.exp(-x**2-y**2)
f_num = sp.lambdify((x,y),f,'numpy')
xx = np.linspace(-1.,2.,1000)
yy = np.linspace(-1.5,1.5,1000)
delta_x = xx[1] - xx[0]
delta_y = yy[1] - yy[0]

XX,YY = np.meshgrid(xx,yy)

zz = f_num(XX,YY)


plt.imshow(zz,extent=[xx.min(), xx.max(), yy.min(), yy.max()])



y_a = 0
y_b = np.pi/4
x_a = sp.cos(2*sp.pi*y)
x_b = y**3
x_a_num = sp.lambdify(y,x_a,'numpy')
x_b_num = sp.lambdify(y,x_b,'numpy')

# try to integrate the inner first. cannot be solved numerically!


result1 = sp.integrate(f,(x,x_a,x_b),(y,y_a,y_b))

# using approximation
eq = sp.Eq(x_a,x_b)
solution_y = sp.nsolve(eq,y,0.2)
solution_x = solution_y**3
print(solution_x,solution_y)

# integrating the slices


# left part

yy_left = np.linspace(y_a,float(solution_y),100)
slices = np.zeros(len(yy_left))
lower_bound = 0
upper_bound = x_a_num(yy_left)

for i,y in enumerate(yy_left):
    upper = upper_bound[i]
    xx = np.linspace(lower_bound,upper,100)
    heights = f_num(xx,y)
    slices[i] = sip.integrate.trapezoid(heights,xx)

area_left = sip.integrate.trapezoid(slices,yy_left)

# right part
yy_right = np.linspace(float(solution_y),y_b,100)
slices = np.zeros(len(yy_right))
lower_bound = x_a_num(yy_right)
upper_bound = x_b_num(yy_right)

for i, y in enumerate(yy_right):
    upper = upper_bound[i]
    lower = lower_bound[i]
    xx = np.linspace(lower, upper, 100)
    heights = f_num(xx, y)
    slices[i] = sip.integrate.trapezoid(heights, xx)

area_right = sip.integrate.trapezoid(slices, yy_right)

total = area_left + area_right
print(total)

# using a mask

left_mask = (
    (YY>0)&(YY<solution_y)&(XX>0)&(XX<x_a_num(YY))
)

right_mask = (
(YY>solution_y)&(YY<y_b)&(XX>x_a_num(YY))&(XX<x_b_num(YY))
)

total_mask = left_mask | right_mask
total2 = np.sum(zz[total_mask])*delta_x*delta_y
print(total2)
plt.show()