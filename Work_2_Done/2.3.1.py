'''
Найдите евклидово расстояние между двумя Series
(точками) a и b, не используя встроенную формулу
'''
import math

x = (5, 6, 7)

y = (8, 2, 9)

#zip - объединяет элементы из нескольких источников данных

distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
print("Euclidean distance from x to y: ",distance)
