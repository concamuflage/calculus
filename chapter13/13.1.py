import numpy as np
a = -0.5
b = np.pi
n = 14
delta = (b-a) / 14
break_1 = [ a + x* delta for x in range(n+1)]
break_2 = np.linspace(a,b,n+1)
print(break_1)
print(break_2)

