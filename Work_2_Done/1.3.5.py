from random import randrange as rnd
import numpy as np 
n = 10
a = [rnd(1000) for x in range(n)]
print(a)
print("Sorted mass")
print(sorted(a, reverse= True))
