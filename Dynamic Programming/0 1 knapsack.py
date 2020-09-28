

# def knapsack(capacity, val, weight):
#     w, v = len(weight), capacity
#     dp = [[0] * (v+1) for _ in range(w+1)]
#     for i in range(1, w+1):
#         for j in range(1, v+1):
#             if j - weight[i-1] < 0:
#                 dp[i][j] = dp[i-1][j]
#             else:
#                 dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i-1]]+val[i-1])
#     print(dp)
#     return dp[-1][-1]


# to compress the status in a reverse way in order to avoid being influencing by the
# previous variable since one item can only be used at once

def knapsack(capacity, val, weight):
    w, v = len(weight), capacity
    dp = [0] * (v+1)
    for i in range(1, w+1):
        for j in range(v, 0, -1):
            if j - weight[i-1] > -1:
                dp[j] = max(dp[j], dp[j - weight[i-1]] + val[i-1])
        print(dp)
    return dp[-1]


capacity = 5
weight = [2, 1, 3]
value = [4, 2, 3]
print(knapsack(capacity, value, weight))
