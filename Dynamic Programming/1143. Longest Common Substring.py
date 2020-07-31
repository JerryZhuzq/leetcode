class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [0] * l1
        for m in range(l2):
            previous, current = 0, 0
            for n in range(l1):
                previous, current = current, dp[n]
                if text1[n] == text2[m]:
                    dp[n] = previous + 1
                else:
                    if n > 0:
                        dp[n] = max(dp[n - 1], dp[n])
        return dp[l1 - 1]
