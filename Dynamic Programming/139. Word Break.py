class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [0] * n
        for i in range(n):
            if i == 0 or dp[i-1] == 1:
                for j in wordDict:
                    if s[i:i+len(j)] == j:
                        dp[i+len(j)-1] = 1
        return dp[-1]