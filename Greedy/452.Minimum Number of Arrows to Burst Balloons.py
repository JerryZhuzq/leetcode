class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        pre = float('-inf')
        points.sort(key=lambda x: x[1])
        res = 0
        for x, y in points:
            if x > pre:
                res += 1
                pre = y

        return res
