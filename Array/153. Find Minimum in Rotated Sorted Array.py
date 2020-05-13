class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                return nums[i]
        return nums[0]

    def findMin_logn(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1

        while True:
            if end - start <= 1:
                return min(nums[start], nums[end])

            mid = (start + end) // 2

            if nums[mid] > nums[start]:
                if nums[mid] < nums[end]:
                    return nums[start]
                start = mid + 1
            else:
                end = mid

    # First solution is to iterate the whole list from left to right, find the first number to descend
    # Second solution using division to find the minimum