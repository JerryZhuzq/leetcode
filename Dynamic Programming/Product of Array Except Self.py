'''
Given an array nums of n integers where n > 1,  return an array output such that output[i]
is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of
the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as
extra space for the purpose of space complexity analysis.)
'''

'''
For [1,2,3,4], we construct an output list which is [0, 24, 12, 4]. The number of the second list stands
for numbers multiply each other from back to front. And we need another variable temp memorizes the number
backwards. Initial temp = 1. Temp *= nums[i], res[i] = temp * res[i+1], res[-1] = temp
     list             temp
0   [0, 24, 12, 4]      1
1   [24, 24, 12, 4]     1 
2   [24, 12, 12, 4]     2
3   [24, 12, 8, 4]      6
4   [24, 12, 8, 6]      meaningless

#Dynamic Programming Backwards
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [0] * l
        temp = 1

        res[-1] = nums[-1]
        for i in range(2, l):
            res[-i] = nums[-i] * res[-i + 1]
        for i in range(l - 1):
            res[i] = temp * res[i + 1]
            temp *= nums[i]
        res[-1] = temp
        return res