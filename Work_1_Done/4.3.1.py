from matplotlib import pyplot as plt
import numpy as np

from scipy.integrate import simps
from numpy import trapz
import random

med_arr = []

n, m, sum = 1, 3, 0

x = np.abs([random.random() for i in range(m) for i in range(n)])
print(" x", x)

med_arr = sorted(x)
print("Mass sort", med_arr)

if m % 2 == 0:
	med = med_arr[m // 2]
else:
	med = med_arr[m // 2]
print("Mediana", med)

for i in range(m):
	sum += x[i]
print("Sredn znach", sum / m)
plt.grid()
plt.scatter(med_arr, med_arr)
plt.show()
