class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2  # avoid overflow
            if nums[mid] == nums[left] == nums[right]:  # duplicates at both sides
                left += 1
                right -= 1
            elif nums[mid] <= nums[right]:
                right = mid
            elif nums[mid] >= nums[left]:
                left = mid + 1

        return nums[left]

# The corner cases lie at duplicates at both sides 22201222