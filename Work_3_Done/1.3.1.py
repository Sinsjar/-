import itertools
import numpy as np

def count_distance(x, y):
    print(f'Евклидово между {x}, {y}:', np.linalg.norm(x - y))
    print(f'Квадрат Евклидова между {x}, {y}:', np.linalg.norm(x - y) ** 2)
    print(f'Чебышева между {x}, {y}:', np.linalg.norm(x - y, ord=np.inf))
    print(f'Хемминга между {x}, {y}:', np.linalg.norm(x - y, ord=1))
    print('#' * 10)


a = np.array([0, 0, 0])
b = np.array([1, 1, 1])
c = np.array([1, 0, 1])
d = np.array([0, 1, 0])

combos = itertools.combinations([a, b, c, d], 2)
for combo in combos:
    count_distance(combo[0], combo[1])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(*a)
ax.scatter(*b)
ax.scatter(*c)
ax.scatter(*d)
plt.show()
