class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        index = 0
        reverse = True
        if l > 1:
            for i in range(l-2,-1,-1):
                if nums[i] < nums[i+1]:
                    index = i
                    reverse = False
                    break
            if not reverse:
                for i in range(l-1, index, -1):
                    if nums[i] > nums[index]:
                        nums[i], nums[index] = nums[index], nums[i]
                        nums[index+1:] = list(reversed(nums[index+1:]))
                        break
            else:
                nums.reverse()