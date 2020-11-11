class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        pre = float('-inf')
        res = 0
        for x, y in intervals:
            if x >= pre:
                pre = y
            else:
                res += 1
        return res
