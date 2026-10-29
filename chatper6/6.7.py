import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

x = np.linspace(-1.5,4.9,10000)
left_of_zero = np.where(x < 0)[0][-1]

_,axes = plt.subplots(1,3)
# define the function
def f(x):
    # x is an array

    piece1 = np.exp(2*np.cos(2*x))
    # generate an array of len(x), each element is 0.0
    piece2 = np.zeros_like(x,dtype=float)

    # an array of true/false
    mask = x>0
    # only calculates the log part for positive x
    second_part = np.log(x[mask]**2)
    # when mask is true, replace with piece2 value 0s with second part values.
    piece2[mask] = second_part
    return piece1 - piece2

# use grid search to find the critical points
y = f(x)

# the following line is extremely important.
# without this line, there will be a very large derivative around x
# which is an artifact, not a true derivative.
# without this line
# the y[right_of_zero]-y[left_of_zero]/dx is going to be very large.
# making the derivative at right_of_zero extremely large
y[left_of_zero]=np.nan
df = np.diff(y)/(x[1]-x[0])

# find the points where the df is minimum
upside_down=-np.abs(df)
# putative critical points: including both
# the local maximum of the upside_down df and
# the x values where f'(x) = 0
dfLocalMin=find_peaks(upside_down)[0]

# remove the local maximum with this test
real_critical =[]
for index in dfLocalMin:
    if np.sign(df[index-1])+np.sign(df[index+1])==0:
        real_critical.append(index)

real_critical=np.array(real_critical)+1

# another critical point where the derivative doesn't exist
# this is obtained through observation of the graph of the function
# we can see that there is a jump point a 0.

# find x that is just before 0


real_critical = np.append(real_critical,left_of_zero)

critical_x = x[real_critical]
critical_y = y[real_critical]

# find inflection points
ddf = np.diff(df)/(x[1]-x[0]) # second derivative
upside_down_2 = -np.abs(ddf)
candidates = find_peaks(upside_down_2)[0]
roots = []
for c in candidates:
    if ddf[c-1]*ddf[c+1]<0:
        roots.append(c)

roots = np.array(roots)
roots = roots+1
inflection_x = x[roots]
inflection_y = y[roots]


axes[0].plot(x, f(x), 'o')
axes[0].plot(critical_x,critical_y,'ro')
axes[0].plot(inflection_x,inflection_y,'bo')

# without limiting y, the extremely small derivative will make the
# graph not centered vertically.
axes[1].set(

    xlabel='$x$',

    xlim=x[[0,-1]],

    ylim=[-15,15],   # ← important

    ylabel=r'$dy\,/\,dx$'

)
axes[1].plot(x[1:],df,'ro')
print(real_critical)
critical_df = df[real_critical]

axes[1].plot(x[real_critical],critical_df,'bo')
axes[1].plot(0,0,'ko',markerfacecolor='w',markersize=9) # jump discontinuity

axes[2].set(

    xlabel='$x$',

    xlim=x[[0,-1]],

    ylim=[-20,20],   # ← important

    ylabel=r'$dy\,/\,dx$'

)


axes[2].plot(x[2:],ddf,'ro')
inflection_ddf = ddf[roots]
axes[2].plot(x[roots],inflection_ddf,'bo')

plt.show()

