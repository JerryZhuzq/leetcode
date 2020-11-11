from heapq import *

# def max_height(N, buildings, heights):
#
#     hp = [(0,0,1)]
#     built = {}
#     built[1] = 0
#
#     for b, h in zip(buildings, heights):
#         hp.append((h, 0, b))
#         built[b] = h
#     heapify(hp)
#
#     while hp:
#         h, seq, b = heappop(hp)
#         if b-1 > 0:
#             if b-1 not in built or (b-1 in built and built[b-1] > h+1):
#                 built[b-1] = h+1
#                 heappush(hp, (h+1, seq+1, b-1))
#         if b+1 <= N:
#             if b+1 not in built or (b+1 in built and built[b+1] > h+1):
#                 built[b+1] = h+1
#                 heappush(hp, (h + 1, seq + 1, b + 1))
#     return max(built.values())

def max_height(N, buildings, heights):
    dp = [float('inf')] * (N+1)
    constraints = {}
    for b, h in zip(buildings, heights):
        constraints[b] = h
    constraints[1] = 0

    for i in range(1, N+1):
        if i in constraints:
            dp[i] = min(dp[i-1] + 1, constraints[i])
        else:
            dp[i] = dp[i-1] + 1

    for i in range(N - 1, 0, -1):
        if i in constraints:
            dp[i] = min(dp[i+1] + 1, constraints[i])
        else:
            dp[i] = min(dp[i+1] + 1, dp[i])
    return max(dp[1:])




def max_height_dp(N, buildings, heights):
    constraints = {}

    dp = [float('inf')] * (N+1)
    for b, h in zip(buildings, heights):
        constraints[b] = h
    constraints[1] = 0
    for i in range(1, N+1):
        if i in constraints:
            dp[i] = min(dp[i-1]+1, constraints[i])
        else:
            dp[i] = dp[i-1] + 1

    for i in range(N-1, 1, -1):
        dp[i] = min(dp[i], dp[i + 1] + 1)
    return max(dp[1:])


# print(max_height(10, [3,8], [1,1]))
# print(max_height_dp(3, [2,3], [10000,10000]))
# print(max_height_dp(1000, [], []))
# print(max_height(1234, [1, 24, 500, 1000], [10000, 10000, 10000, 10000]))



def codeHere(inputData):
    # Use the function to return the solution.
    input = inputData.replace("\n", ' ')
    input_list = input.split(' ')
    N, M = int(input_list[0]), int(input_list[1])
    res = [str(x) for x in range(1, N+1)]
    for i in range(2, len(input_list), 3):
        A, B, C = int(input_list[i]), int(input_list[i+1]), int(input_list[i+2])
        list_A = res[:A]
        list_B = res[A:A+B]
        tmp = (list_A + res[A+B:])
        list_C, list_rm_C = tmp[:C], tmp[C:]
        res = list_C + list_B[::-1] + list_rm_C
    return ' '.join(res)


x = [1,2]
y = x
x.append(2)
print(y)

a = [["5","3","0", "2","7","6", "4","1","8"],
     ["6","2","4", "1","9","5", "3","0","7"],
     ["1","9","8", "3","4","0", "5","6","2"],

     ["8","1","2", "7","6","4", "0","5","3"],
     ["4","0","6", "8","5","3", "7","2","1"],
     ["7","5","3", "0","2","1", "8","4","6"],

     ["0","6","1", "5","3","7", "2","8","4"],
     ["2","8","7", "4","1","9", "6","3","5"],
     ["3","4","5", "6","8","2", "1","7","9"]]




