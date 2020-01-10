class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] >= n - 1:
            return 1
        res = 1
        anchor = nums[0]
        max_jump = 0
        for i in range(1, n):
            max_jump = max(max_jump, i + nums[i])
            # print(max_jump, i, n)
            if max_jump >= n - 1:
                return res + 1
            if i == anchor:
                anchor = max_jump
                res += 1
