class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1 for i in range(n+1)]
        memo[0], memo[1] = 1, 1
        for i in range(2,n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]
    # bottom-top


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1 for i in range(n+1)]
        memo[0], memo[1] = 1, 1
        def calWays(n):
            if memo[n] == -1:
                memo[n] = calWays(n-1) + calWays(n-2)
            return memo[n]
        return calWays(n)
    # top-down