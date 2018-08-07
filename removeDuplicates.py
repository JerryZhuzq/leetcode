# 从排序数组中删除冗余项
class Solution(object):
    def removeDuplicates(self,nums):
        i = 0
        while (i < len(nums)):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    nums.pop(j)
                    continue
#                   pop操作后j大小无需增加，len(nums)大小同时在减小
                j = j + 1
            i = i + 1
        return nums
# 可实现非排序下的冗余数组元素删除


# 两个指针，一个快指针，一个慢指针
    def removeDuplicates1(self,nums):
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i = i + 1
                nums[i] = nums[j]
        return i + 1

i = Solution()
nums = [0,0,0,1,1,2,4,2,3]
print(i.removeDuplicates(nums))