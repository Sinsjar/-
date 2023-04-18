import numpy as np
'''
Создать матрицу с 0 внутри, и 1 на границах.
'''

a = np.ones((6, 6))
a[1:-1, 1:-1] = 0
print(a)
