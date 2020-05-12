a = range(11)
for i in range(10,-1,-1):
    print(a[i], i)
# import sys
# line = sys.stdin.readline().strip()
# numbers = line.split()
# n, m = int(numbers[0]), int(numbers[1])
#
# print(int(m/(2-2**(1-n))))
#
# import sys
# import math
# line1 = sys.stdin.readline().strip()
# numbers = sys.stdin.readline().strip()
# K = int(line1)
# line2 = numbers.split()
# A, X, B, Y = int(line2[0]),int(line2[1]),int(line2[2]),int(line2[3])
#
# def comb(x ,y):
#     return math.factorial(x)/(math.factorial(x-y)*math.factorial(y))
#
#
# limit_A = K // A
# count = []
# for i in range(limit_A+1):
#     temp_B = (K - (A*i)) % B
#     if temp_B == 0:
#         count.append((i, (K - (A*i))//B))
# res = 0
# for a, b in count:
#     res += (comb(X, a) * comb(Y, b))
# print(int(res % 1000000007))
#
