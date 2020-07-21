class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s3[j - 1] == s2[j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s3[i - 1] == s1[i - 1]
                else:
                    dp[i][j] = (dp[i - 1][j] and s3[i + j - 1] == s1[i - 1]) or (
                                dp[i][j - 1] and s3[i + j - 1] == s2[j - 1])

        return dp[-1][-1]

# build a 2D dp and find a path which leads to the final answer

