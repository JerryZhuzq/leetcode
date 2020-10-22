def divide(n, k):
    dp = [[[-1]*50 for _ in range(50)] for _ in range(50)]

    def helper(s, n, k):

        if k == 0:
            if n == 0:
                return 1
            return 0

        if n == 0:
            return 0

        if dp[k][n][s] != -1:
            return dp[k][n][s]

        res = 0
        for i in range(s, n//k+1):
            res += helper(i, n-i, k-1)
        dp[k][n][s] = res

        return res
    res = helper(1, n, k)
    return res


print(divide(8, 4))
