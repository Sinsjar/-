import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
from numpy import trapz

x = np.arange(1, 10, 1)

y = np.abs(np.fabs(np.cos(x * np.exp(np.cos(x) + np.log(x + 1)))))

plt.grid()
plt.plot(x, y, c = "r")
plt.fill_between(x, y)

area = trapz(y)
print(area)
plt.show()
