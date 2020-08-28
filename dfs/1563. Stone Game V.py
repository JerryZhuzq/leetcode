class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        dp = [[0]*n for _ in range(n)]
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1]+stoneValue[i])
        def dfs(l, r):
            res = 0
            if l == r:
                dp[l][r] = stoneValue[l]
                return 0
            if dp[l][r] != 0:
                return dp[l][r]
            for i in range(l, r):
                sum_left, sum_right = prefix[i+1]-prefix[l], prefix[r+1]-prefix[i+1]
                if sum_left < sum_right:
                    res = max(res, sum_left + dfs(l, i))
                elif sum_left == sum_right:
                    res = max(res, sum_left + max(dfs(l, i), dfs(i+1, r)))
                else:
                    res = max(res, sum_right + dfs(i+1, r))
            dp[l][r] = res
            return res
        return dfs(0, n-1)

# dfs + memo
