

# import libraries and define global settings
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# define global figure properties used for publication
import matplotlib_inline.backend_inline
matplotlib_inline.backend_inline.set_matplotlib_formats('svg') # display figures in vector format
plt.rcParams.update({'font.size':14,             # font size
                     'savefig.dpi':300,          # output resolution
                     'axes.titlelocation':'left',# title location
                     'axes.spines.right':False,  # remove axis bounding box
                     'axes.spines.top':False,    # remove axis bounding box
                     'lines.linewidth':2         # increase default line thickness
                     })


# function (as a function)
def fx(x): return 3*x**2 - 2*x + np.pi

# derivative function
def df(x): return 6*x - 2

# x-axis grid
x = np.linspace(-1,2,2001)

# random starting point
localmin = -1
startloc = localmin + 0 # adding 0 makes a copy

# learning parameters
learning_rate = 0.2
training_epochs = 100

trajectory = []
# run through training
for i in range(training_epochs):
  grad = df(localmin)
  localmin = localmin - learning_rate*grad
  trajectory.append(localmin)

print(f'Initial guess:  (x,y) = ( {startloc:.3f},{fx(startloc):.3f} )')
print(f'Final estimate: (x,y) = ( {localmin:.3f},{fx(localmin):.3f} )')
print(f'Numpy minimum:  (x,y) = ( 1/3,{fx(1/3):.3f} )') # numerically evaluated

# plot the results

plt.figure(figsize=(10,5))
trajectory = np.array(trajectory)
plt.plot(x,fx(x),'k',label=r'$f(x) = 3x^2 - 2x + \pi$')
plt.plot(x,df(x),'--',color=[.4,.4,.4],label=r"$f\,'(x) = 6x-2$")

# plot the guesses
plt.plot(trajectory,fx(trajectory),'ko')
plt.plot(trajectory,df(trajectory),'ko')
plt.plot(startloc,fx(startloc),'ks',markersize=9,markerfacecolor=[.7,.7,.7],label='Initial guess')
plt.plot(localmin,fx(localmin),'ko',markersize=9,markerfacecolor='w',label='Final estimate')
plt.plot(localmin,df(localmin),'ko',markersize=9,markerfacecolor=[.9,.9,.9])


plt.gca().set(xlim=x[[0,-1]],ylim=[-10,12],xlabel='$x$',ylabel="$f$ or $f\,'$")
plt.grid(color=[.9,.9,.9])
plt.legend()

plt.tight_layout()
plt.savefig('critpnts_gradientDescent.png')
plt.show()