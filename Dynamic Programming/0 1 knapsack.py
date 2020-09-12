def knapsack(capacity, val, weight):
    n = len(weight)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-weight[j-1]]+val[j])