# import sys
# from collections import defaultdict
# import heapq
# n = int(sys.stdin.readline())
# idx_x = defaultdict(list)
# q = []
# x = list(map(int, sys.stdin.readline().split(' ')))
# for i, val in enumerate(x):
#     if val not in idx_x:
#         heapq.heappush(q, val)
#     heapq.heappush(idx_x[val], i)
#
a = [[0] * 4 for _ in range(3)]

print(a)
# def f(nums):
#     for i in range(1, len(nums)):
#         nums[i] = min(nums[i - 1], nums[i])
#     return sum(nums)