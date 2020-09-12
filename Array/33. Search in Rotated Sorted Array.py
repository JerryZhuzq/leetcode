class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2  # two extreme
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                if nums[l] < nums[mid]:
                    l = mid
                else:
                    if nums[l] > target:
                        l = mid
                    else:
                        r = mid
            else:
                if nums[l] < nums[mid]:
                    if target < nums[l]:
                        l = mid
                    else:
                        r = mid
                else:
                    r = mid
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2  # two extreme
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                if nums[l] <= nums[mid]:
                    l = mid + 1
                else:
                    if nums[l] > target:
                        l = mid + 1
                    else:
                        r = mid
            else:
                if nums[l] <= nums[mid]:
                    if target < nums[l]:
                        l = mid + 1
                    else:
                        r = mid
                else:
                    r = mid
        return l if nums[l] == target else -1
