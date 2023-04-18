import numpy as np


a = np.ones((3, 3))

print("Доска")
x = np.zeros((8, 8), dtype = int)
x[1::2, ::2] = 1
x[::2, 1::2] = 1
print(x)
