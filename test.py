import heapq

a = ["JFK","ERD","JFK","SFO","ATL","SFO"]
heapq.heapify(a)
a[0] = a[0][1:]
heapq.heapify(a)
print(a)
