import math
# line = input()
# try:
#     m, n = list(map(int, line.split()))
# except:
#     print([])
# if m < 10 or m >1000 or n < 10 or n > 1000:
#     print([])
#
# total_length, current_length = m * n, 0
# offset = 0
# store = []
# while (m-2*offset) >= 1 and (n-2*offset) >= 1:
#     if (m-2*offset) == 1 or (n-2*offset) == 1:
#         for i in range(offset, m-offset):
#             for j in range(offset, n-offset):
#                 store.append([i, j])
#         break
#     for i in range(offset, n-offset-1):
#         store.append([offset, i])
#     for i in range(offset, m-offset-1):
#         store.append([i, n-offset-1])
#     for i in range(offset, n-offset-1):
#         store.append([m-offset-1, n-i-1])
#     for i in range(offset, m-offset-1):
#         store.append([m-i-1, offset])
#     offset += 1
# res = []
# for i in range(len(store)):
#     if i+1 > 10:
#         num = str(i+1)
#         if num[-1] == '7' and int(num[-2]) % 2 == 1:
#             res.append(store[i])
# print(res)


# line = input()
# m, n = list(map(int, line.split(' ')))
# print(m, n)
# if m < 10 or m > 1000 or n < 10 or n > 1000:
#     print([])
# total_length, current_length = m * n, 0
# offset = 0
# store = []
# while (m-2*offset) >= 1 and (n-2*offset) >= 1:
#     if (m-2*offset) == 1 or (n-2*offset) == 1:
#         for i in range(offset, m-offset):
#             for j in range(offset, n-offset):
#                 store.append([i, j])
#         break
#     for i in range(offset, n-offset-1):
#         store.append([offset, i])
#     for i in range(offset, m-offset-1):
#         store.append([i, n-offset-1])
#     for i in range(offset, n-offset-1):
#         store.append([m-offset-1, n-i-1])
#     for i in range(offset, m-offset-1):
#         store.append([m-i-1, offset])
#     offset += 1
# print(store)
# res = []
# for i in range(len(store)):
#     if i+1 > 10:
#         num = str(i+1)
#         if num[-1] == '7' and int(num[-2]) % 2 == 1:
#             res.append(store[i])
# print(res)

# from collections import defaultdict
# import math
#
# line = int(input())
# lines = input()
# nodes = list(map(int, lines.split(' ')))
# store = defaultdict(int)
# for n in nodes:
#     store[n] += 1
# pre = 0
# res = 1
# for i in sorted(store.keys()):
#     if i == 0:
#         continue
#     else:
#         res = res*(math.factorial(store[pre]*2)/(math.factorial(store[i])*math.factorial(store[pre]*2-store[i])))
#         pre = i
#
# print(int(res))
a, b = "21", "12"
