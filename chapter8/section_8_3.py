import numpy as np
import sympy as sp

from section_8_2 import MVTandPlot
from section_8_1 import x

if __name__ == '__main__':
    fx = sp.sin(x)
    hx = (2*x)/(2*x**2+1)**2
    # MVTandPlot(fx, 0, 1.8 * np.pi)
    MVTandPlot(hx, -2, 1)

