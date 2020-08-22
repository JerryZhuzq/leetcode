class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        from functools import lru_cache
        nums = [1] + nums + [1]
        @lru_cache(None)
        def dp(left, right):
            if left + 1 == right:
                return 0
            return max(nums[i]*nums[left]*nums[right] + dp(left, i) + dp(i, right) for i in range(left+1, right))
        return dp(0, len(nums)-1)

# dp Top-down, to return the maximum number of coins obtainable in the open interval
# (left, right). From top to bottom

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for left in range(n-2, -1, -1):
            for right in range(left+2, n):
                dp[left][right] = max(nums[left] * nums[right] * nums[i] + dp[left][i] + dp[i][right] for i in range(left+1, right))
        return dp[0][n-1]