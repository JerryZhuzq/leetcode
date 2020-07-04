class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)

        def helper(nums1, nums2, k):
            if not nums1:
                return nums2[k]
            if not nums2:
                return nums1[k]
            mid1 = len(nums1) // 2
            mid2 = len(nums2) // 2

            if k > mid1 + mid2:
                if nums1[mid1] > nums2[mid2]:
                    return helper(nums1, nums2[mid2 + 1:], k - 1 - mid2)
                else:
                    return helper(nums1[mid1 + 1:], nums2, k - 1 - mid1)

            else:
                if nums1[mid1] > nums2[mid2]:
                    return helper(nums1[:mid1], nums2, k)
                else:
                    return helper(nums1, nums2[:mid2], k)

        if total_length % 2 == 1:
            return helper(nums1, nums2, total_length // 2)
        else:
            return (helper(nums1, nums2, total_length // 2) + helper(nums1, nums2, total_length // 2 - 1)) / 2
