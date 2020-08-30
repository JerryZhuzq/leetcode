class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        dp = [0] * len(text1)
        for i in range(len(text2)):
            previous = 0
            for j in range(len(text1)):
                if text1[j] == text2[i]:
                    dp[j], previous = previous + 1, dp[j]
                else:
                    previous = dp[j]
                    if j > 0:
                        dp[j] = max(dp[j], dp[j - 1])
        return dp[-1]
