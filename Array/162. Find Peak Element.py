class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def binary_search(left, right):
            if left == right:
                return left

            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:    # the corner case 0, n-1 could be solved here, since for 0, 1 this case,
                                             # mid == 0 and we don't need to worry about nums[-1]
                return binary_search(left, mid)
            else:
                return binary_search(mid + 1, right)

        return binary_search(0, len(nums) - 1)
