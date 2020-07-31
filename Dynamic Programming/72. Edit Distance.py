class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(1,len(word1)+1):
            dp[i][0] = i
        for j in range(1,len(word2)+1):
            dp[0][j] = j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]-1, dp[i][j-1])+1 #why?
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        return dp[-1][-1]


# If we have corner issue with out dp list, just increase its capacity to
# dp[i+1][j+1] and remember to initialize their values
# This is a Levenshtein distance problem, try to figure out how the dp value changes
# after encounter same or different value
