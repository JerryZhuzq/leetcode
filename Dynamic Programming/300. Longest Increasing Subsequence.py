class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 1:
            return 0
        dp = [1 for _ in range(n)]
        res = 1
        for i in range(n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        for i in dp:
            res = max(res, i)
        return res

# dp Bottom-Up

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 1:
            return 0
        dp = [0 for _ in range(n + 1)]
        res = 1

        def subLIS(nums, k):
            if k == 0:
                return 1
            if dp[k] != 0:
                return dp[k]
            l = 1
            for i in range(k - 2, -1, -1):
                if nums[k - 1] > nums[i]:
                    l = max(l, 1 + subLIS(nums, i + 1))
            dp[k] = l
            return l

        for i in range(n, 0, -1):
            subLIS(nums, i)
        for i in dp:
            res = max(res, i)
        return res

# Memorization Top-Down

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def binarySearch(t):
            left, right = 0, len(c) - 1
            mid = (left + right) // 2

            while (left < right):
                if c[mid] > t:
                    right = mid
                elif c[mid] < t:
                    left = mid + 1
                else:
                    c[mid] = t
                    return
                mid = (left + right) // 2
            # process when left == right
            if mid == len(c) - 1 and t > c[mid]:
                c.append(t)
            else:
                c[mid] = t

        if len(nums) < 1:
            return 0
        c = [nums[0]]
        for i in range(1, len(nums)):
            binarySearch(nums[i])
        return len(c)

# DP with binary search. Maintain a list to store the right position for every number in nums,
# but only the length of the list matters, the sequence of list means nothing.