'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(nums, target, start):
            l = len(nums)
            p = l // 2
            if not nums:
                return -1
            if nums[p] == target:
                return start+p
            if nums[p] > nums[0]:
                if target > nums[p]:
                    return helper(nums[p+1:], target, start+p+1)
                else:
                    if target < nums[0]:
                        return helper(nums[p+1:], target, start+p+1)
                    else:
                        return helper(nums[:p], target, start)
            else:
                if target > nums[p]:
                    if target < nums[0]:
                        return helper(nums[p+1:], target, start+p+1)
                    else:
                        return helper(nums[:p], target, start)
                else:
                    return helper(nums[:p], target, start)
        return helper(nums, target, 0)