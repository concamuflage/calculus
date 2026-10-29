import numpy as np

nums = [x for x in range(1,11)]
print(nums)

cum_sum = []
for x in nums:
    if x == 1:
        cum_sum.append(x)
    else:
        cum = cum_sum[-1] + x
        cum_sum.append(cum)


cum_sum_2=np.cumsum(nums)

print(cum_sum)
print(cum_sum_2)
