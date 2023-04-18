import numpy as np

x = np.zeros((5, 5))

print("Массив: ")
print(x)

print("Массив с изменёнными значениями")
x += np.arange(5)
print(x)
