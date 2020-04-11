class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        temp = set()
        res = [[]]
        nums.sort()
        for i in range(1,len(nums)+1):
            for j in combinations(nums, i):
                if j not in temp:
                    temp.add(j)
                    res.append(list(j))
        return res


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def helper(cur, path):
            res.append(cur)
            for i in range(len(path)):
                if i > 0 and path[i - 1] == path[i]:
                    continue
                helper(cur + [path[i]], path[i + 1:])

        helper([], nums)  nn m

