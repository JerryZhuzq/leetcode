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

'''是找当前列表按照字典顺序排序的下一个排列。思路是从右往左遍历，若找到一个数比右边的数小，
则记录该数的index。再次从右往左遍历，找到第一个比记录值大的数，然后将两个数交换，再将index
右边所有数整体reverse。时间复杂度:O(n) 空间复杂度:O(n) Corner Case在于如果初始列表长度
小于2，那就不需要任何操作；如果列表内数为递减，则要将整个列表reverse。陷阱在于，将两个数交换
后，不太能理解将之后部分的数组reverse，因为这个字典顺序排序里的下一个排序，所以之后部分数组要
做到是最小值，也就是将原来的递减变换为递增。'''