class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for i in range(len(nums)):
            l, r = 0, len(dp)-1
            while l <= r:
                mid = l + (r-l) // 2
                if dp[mid] == nums[i]:
                    break
                elif dp[mid] > nums[i]:
                    r = mid - 1
                elif dp[mid] < nums[i]:
                    l = mid + 1
            if l == len(dp):
                dp.append(nums[i])
            else:
                dp[l] = min(dp[l], nums[i])
        return len(dp)


# image it's a 扑克接龙