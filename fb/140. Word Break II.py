class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        ans = []
        dp = {}

        def helper(cur_s, i):
            if i in dp:
                for x in dp[i]:
                    ans.append(cur_s + x)
                return dp[i]
            dp[i] = []
            for t in range(i, len(s)):
                if s[i:t + 1] in wordSet:
                    if t == len(s) - 1:
                        ans.append(cur_s + s[i:t + 1])
                        dp[i].append(s[i:t + 1])
                    else:
                        temp = helper(cur_s + s[i:t + 1] + ' ', t + 1)
                        for x in temp:
                            dp[i].append(s[i:t + 1] + ' ' + x)
            return dp[i]

        helper('', 0)
        return ans
