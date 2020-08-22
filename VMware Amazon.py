
from itertools import combinations
from math import factorial
def numOfTeam(num, skills, minAsso, minLevel, maxLevel):
    candidate = []
    for i in skills:
        if i >= minLevel and i <= maxLevel:
            candidate.append(i)
    res = 0
    n = len(candidate)
    if n >= minAsso:
        for i in range(minAsso, n+1):
            res += (factorial(n)/(factorial(i)*factorial(n-i)))
    return int(res)

# print(numOfTeam(6, [12,4,6,13,5,10],3,4,10))

class Solution():

    def __init__(self):
        self.res = 0

    def paritionPrime(self, num):
        def isPrime(num):
            if num == 1:
                return False
            elif num == 2 or num == 3:
                return True
            else:
                n = 2
                while n*n <= num:
                    if num % n == 0:
                        return False
                    n += 1
                return True

        def partition(num):
            if not num:
                self.res += 1
            for i in range(len(num)):
                n = int(num[:i+1])
                if isPrime(n):
                    # print(n)
                    partition(num[i+1:])
        partition(num)
        return self.res
i = Solution()
j = Solution()
k = Solution()
# print(i.paritionPrime('11373'))
# print(j.paritionPrime('3175'))
# print(k.paritionPrime('24'))


import heapq

# from collections import defaultdict
# def debtRecord(numRows, numCols, debts):
#     record = defaultdict(int)
#     for b, l, a in debts:
#         record[b] -= a
#         record[l] += a
#     smallest_val = 0
#     smallest_list = []
#     for i in record:
#         if record[i] < 0:
#             if record[i] < smallest_val:
#                 smallest_val = record[i]
#                 smallest_list.clear()
#                 smallest_list.append(i)
#             elif record[i] == smallest_val:
#                 smallest_list.append(i)
#     if len(smallest_list) == 0:
#         return ['Nobody has a negative balance']
#     smallest_list.sort()
#     print(record)
#     return smallest_list
#
#
# debts = [['Alex', 'Blake', 2], ['Blake', 'Alex', 2], ['Casey', 'Alex', 5],
#          ['Blake', 'Casey', 7], ['Alex', 'Blake', 4], ['Alex', 'Casey', 4]]
# print(debtRecord(6, 2, debts))

# def maxOfMinElevations(columnCount, rowCount, mat):
#     # WRITE YOUR CODE HERE
#     direction = [[1,0], [0, 1]]
#     dp = [[-1] * columnCount for _ in range(rowCount)]
#     def dfs(i, j, val):
#         for x, y in direction:
#             if x+i < rowCount and y+j < columnCount:
#                 if dp[x+i][y+j] == -1:
#                     if mat[x+i][y+j] >= val:
#                         dp[x+i][y+j] = mat[x+i][y+j]
#                         dfs(x+i, y+j, mat[x+i][y+j])
#                     else:
#                         dp[x+i][y+j] = mat[x+i][y+j]
#                         dfs(x+i, y+j, mat[x+i][y+j])
#                 else:
#                     if val > dp[x+i][y+j]:
#                         dp[x+i][y+j] = val
#                         dfs(x+i, y+j, val)
#                     else:
#                         dfs(x+i, y+j, val)
#     dfs(0, 0, 0)
#     return dp[-1][-1]

# def maxOfMinElevations(columnCount, rowCount, mat):
# #     # WRITE YOUR CODE HERE
# #     dp = mat
# #     for i in range(rowCount):
# #         for j in range(columnCount):
# #             if i > 0 and j > 0:
# #                 dp[i][j] = min(mat[i][j], max(dp[i-1][j], dp[i][j-1]))
# #             elif i > 0:
# #                 dp[i][j] = min(mat[i][j], dp[i-1][j])
# #             elif j > 0:
# #                 dp[i][j] = min(mat[i][j], dp[i][j-1])
# #             else:
# #                 dp[i][j] = mat[i][j]
# #     return dp[-1][-1]
# #
# # mat = [[6, 1, 6], [4,5,7],[2,3,8]]
# # # print(maxOfMinElevations(3,3,mat))
# #
# #
# #
# # def hike(m, n, grid):
# #     dp = grid
# #     for i in range(m):
# #         for j in range(n):
# #             if i > 0 and j > 0:
# #                 dp[i][j] = min(grid[i][j], max(dp[i - 1][j], dp[i][j - 1]))
# #             elif i > 0:
# #                 dp[i][j] = min(grid[i][j], dp[i - 1][j])
# #             elif j > 0:
# #                 dp[i][j] = min(grid[i][j], dp[i][j - 1])
# #             else:
# #                 dp[i][j] = grid[i][j]
# #     return dp[m - 1][n - 1]

