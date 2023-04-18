from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import simps
from numpy import trapz
import random


n, m = 1, 10
x = np.abs([random.randint(1, 10) for i in range(m) for i in range(n)])
print(" x", x)

y = np.abs(np.sqrt(1 + np.exp(np.sqrt(x)) + np.cos(x ** 2))) / \
			(np.fabs(1 - (np.sin(x)) ** 3)) + np.log(np.fabs(2 * x))
print(" y" , y)

x2 = x[0: 5: 1]

print("x2", x2)

y2 = np.abs((np.sqrt(1 + np.exp(np.sqrt(x2)) + np.cos(x2 ** 2)))) / \
(np.fabs(1 - (np.sin(x2)) ** 3)) + np.log(np.fabs(2 * x2))

print("y2", y2)

plt.grid()
plt.plot(x, y)

plt.show()
plt.grid()
plt.scatter(x2, y2)
