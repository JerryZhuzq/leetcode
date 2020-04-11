class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        memo = [-1 for x in range(len(nums))]
        memo[0] = nums[0]
        if len(nums) == 1:
            return memo[0]
        memo[1] = max(nums[0], nums[1])
        if len(nums) == 2:
            return memo[1]
        for i in range(2, len(nums) - 1):
            memo[i] = max(memo[i - 2] + nums[i], memo[i - 1])
        res1 = memo[len(nums) - 2]
        memo[1] = nums[1]
        memo[0] = 0
        for i in range(2, len(nums)):
            memo[i] = max(memo[i - 2] + nums[i], memo[i - 1])
        res2 = memo[len(nums) - 1]
        return max(res1, res2)

    # split the list into two nums[0:n-1] and nums[1:n], and compute the optimal value
    # for each sub-list, the max value is the final answer

