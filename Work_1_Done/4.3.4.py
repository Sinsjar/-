from matplotlib import pyplot as plt
import numpy as np


APPLE = [131.99, 121.88, 122.18, 131.5, 124.67, 137.02, 145.84, 151.92, 141.71, 149.87, 166.44, 177.51]

Microsoft = [231.79, 232.42, 237.55, 252.12, 250, 270.98, 285, 302.14, 282.26, 331.83, 333.49, 336.27]

Google =[91.35, 101.1, 103.2, 117.88, 117.85, 122.1, 134.7, 144.83, 133.78, 148, 142.76, 145.05] 

mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

plt.plot(mes, Microsoft, c = "r")

plt.plot(mes, APPLE, c = "g")

plt.plot(mes, Google, c = "b")

plt.grid()

plt.show()
