class Solution:
    def integerBreak(self, n: int) -> int:
        memo = [-1 for x in range(n+1)]
        if n == 1:
            return 1
        def breakInt(n):
            if n == 1:
                return 1
            if memo[n] != -1:
                return memo[n]
            for i in range(1,n):
                memo[n] = max(memo[n],i*(n-i),i*breakInt(n-i))
            return memo[n]
        breakInt(n)
        return memo[n]
    # Top-Down

class Solution:
    def integerBreak(self, n: int) -> int:
        memo = [-1 for x in range(n+1)]
        memo[1] = 1
        for i in range(1,n+1):
            for j in range(1, i):
                memo[i] = max(memo[i],j*(i-j),j*memo[i-j])
        return memo[n]

    #Bottom-Up