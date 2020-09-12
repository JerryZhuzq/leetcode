# import sys
# import heapq
# line = int(sys.stdin.readline().strip())
# sugar1, sugar2 = [], []
# for i in range(line):
#     curline = sys.stdin.readline().strip().split(' ')
#     if int(curline[1]) == 1:
#         sugar1.append([-int(curline[0]),i+1])
#     else:
#         sugar2.append([-int(curline[0]),i+1])
#
# if len(sugar1) < 3 and len(sugar2) < 3:
#     print("null")
# else:
#     heapq.heapify(sugar1)
#     heapq.heapify(sugar2)
#     candy_1, idx_1 = 0, []
#     candy_2, idx_2 = 0, []
#     if len(sugar1) > 2:
#         n = 0
#         while n < 3:
#             num, idx = heapq.heappop(sugar1)
#             candy_1 -= num
#             idx_1.append(str(idx))
#             n += 1
#     if len(sugar2) > 2:
#         n = 0
#         while n < 3:
#             num, idx = heapq.heappop(sugar2)
#             candy_2 -= num
#             idx_2.append(str(idx))
#             n += 1
#     if candy_1 > candy_2:
#         idx_1 = idx_1[::-1]
#         print(' '.join(idx_1))
#         print(str(1))
#         print(str(candy_1))
#     elif candy_1 < candy_2:
#         idx_2 = idx_2[::-1]
#         print(' '.join(idx_2))
#         print(str(2))
#         print(str(candy_2))
#     else:
#         if min(idx_1) < min(idx_2):
#             idx_1 = idx_1[::-1]
#             print(' '.join(idx_1))
#             print(str(1))
#             print(str(candy_1))
#         else:
#             idx_2 = idx_2[::-1]
#             print(' '.join(idx_2))
#             print(str(2))
#             print(str(candy_2))
import sys
k = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())

size = list(map(int, sys.stdin.readline().strip().split(' ')))
value = list(map(int, sys.stdin.readline().strip().split(' ')))
dp = [0 for i in range(k+1)]

for i in range(n):
    for j in range(k,-1,-1):
        if j >= size[i]:
            dp[j] = max(dp[j], dp[j-size[i]]+value[i])
print(str(dp[-1]))


import sys
k = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())

size = list(map(int, sys.stdin.readline().strip().split(' ')))
value = list(map(int, sys.stdin.readline().strip().split(' ')))
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        dp[i][j] = dp[i-1][j]
        if j >= size[i-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-size[i-1]]+value[i-1])
print(str(dp[-1][-1]))
