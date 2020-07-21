class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        mid = (l + r) // 2

        def partition(l, r, target, stat):
            mid = (l + r) // 2
            while (l < r):
                if nums[mid] == target:
                    if stat == 'left':
                        r = mid - 1
                        mid = (l + r) // 2
                    else:
                        l = mid + 1
                        mid = (l + r) // 2
                elif nums[mid] < target:
                    l = mid + 1
                    mid = (l + r) // 2
                else:
                    r = mid - 1
                    mid = (l + r) // 2
            if nums[l] == target:
                return l
            if stat == 'left':
                return l + 1
            else:
                return l - 1

        while (l <= r):
            if nums[mid] > target:
                r = mid - 1
                mid = (l + r) // 2
            elif nums[mid] < target:
                l = mid + 1
                mid = (l + r) // 2
            else:
                left = partition(l, r, target, 'left')
                right = partition(l, r, target, 'right')
                return [left, right]
        return [-1, -1]


# Run time complexity requirement: O(logn) which indicates us using binary search
# Continue to find the mid until left equals right, in the meantime when you update
# the new left or right index, it should be mid-1 or mid+1 since you have already
# testify the mid value
