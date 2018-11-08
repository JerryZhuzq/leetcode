class Solution(object):
    def containsDuplicate(self,nums):
        ifContains = False
        temp = {}
        for i in nums:
            if temp.get(i):
                ifContains = True
                break
            else:
                temp[i] = i
        return ifContains

    def containsDuplicate1(self,nums):
        ifContains = False
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                ifContains = True
                break
        return ifContains

i = Solution()
nums = [1,2,3,5,4,3]
print(i.containsDuplicate1(nums))