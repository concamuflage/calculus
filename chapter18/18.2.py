from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

_,axes = plt.subplots(1,3)

N = 2000
data1 = stats.logistic.rvs(size=N//2)
data2 = stats.wald.rvs(2,size=N//2)

data = np.zeros(N)
data[::2] = data1
data[1::2] = data2
colors = ['r','g','b']

for idx, dataset in enumerate([data1,data2,data]):
    heights, bins = np.histogram(dataset,bins='auto')
    bin_centers = 0.5 * (bins[1:] + bins[:-1])

    pdf_height = heights/N
    cdf_height = np.cumsum(pdf_height)

    axes[1].plot(bin_centers,pdf_height,color = colors[idx])
    axes[2].plot(bin_centers, cdf_height,color = colors[idx])


plt.show()


