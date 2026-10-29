
import matplotlib.pyplot as plt
import numpy as np

# break points
a = -0.5
b = np.pi
n = 14
delta = (b-a) / 14
break_1 = [ a + x* delta for x in range(n+1)]
break_2 = np.linspace(a,b,n+1)


# function
xx = np.linspace(-1,4,100)

def f(x):
    return np.exp(x)/10 +np.cos(x)

for bb in break_1:
    plt.plot([bb,bb],[0,0.05],color = 'black')
shaded_indices = (xx>a) & (xx<b)
shaded_xx = xx[shaded_indices]
shaded_yy = f(shaded_xx)
plt.fill_between(shaded_xx,shaded_yy,color ='gray')
plt.plot(xx,f(xx))
plt.xticks([-1, 0, 1, 2, 3])
plt.xlim([-1,3.5])
plt.ylim([0,2])
plt.vlines(a,0,f(a))
plt.vlines(b,0,f(b))

plt.show()

