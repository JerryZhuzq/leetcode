class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        max_list, max_degree = [], 0
        for num in count:
            if count[num] > max_degree:
                max_list = []
                max_degree = count[num]
                max_list.append(num)
            elif count[num] == max_degree:
                max_list.append(num)
        max_set = set(max_list)
        start_index = {}
        res = 50001
        for i in range(len(nums)):
            if nums[i] in max_set:
                if nums[i] not in start_index:
                    start_index[nums[i]] = [i, i]
                else:
                    start_index[nums[i]][1] = i
        for num in start_index:
            res = min(res, start_index[num][1]-start_index[num][0]+1)
        return res