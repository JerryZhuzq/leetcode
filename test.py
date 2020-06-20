import heapq
from math import sqrt

K = 3
points = []

res = heapq.nsmallest(K, points, key=lambda x: sqrt(x[0] ** 2 + x[1] ** 2))
print(res)