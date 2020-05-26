class Solution:
    def numTrees(self, n: int) -> int:
        if not n:
            return 0
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(1, n + 1):
            res = 0
            for j in range(1, i + 1):
                left = max(dp[j - 1], 1)
                right = max(dp[i - j], 1)
                res += (left * right)
            dp[i] = res
        return dp[n]


# typical bottom-up dynamic programming
