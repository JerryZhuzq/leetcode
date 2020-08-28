class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for i in nums:
            if i-1 not in nums_set:
                cur_num = i
                cur_longest = 1
                while cur_num+1 in nums_set:
                    cur_longest += 1
                    cur_num += 1
                longest = max(longest, cur_longest)
        return longest