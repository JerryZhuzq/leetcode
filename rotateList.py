# 旋转数组
class Solution(object):
    def rotate(self,nums,k):
        temp = nums[0]
        n = k % len(nums)
        for j in range(0,n):
            for i in range(0, len(nums)):
                if i == len(nums) - 1:
                    nums[0] = temp
                else:
                    nums[i + 1], temp = temp, nums[i + 1]
        return nums

    def rotate1(self, nums,k):
        n = k % len(nums)
        nums = nums[len(nums)-n:]+nums[:len(nums)-n]
        return nums
#   数组加减法 翻转数组


i = Solution()
nums = [1,2,3,4,5,6,7]
print(i.rotate1(nums,34))

