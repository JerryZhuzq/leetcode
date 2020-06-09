class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda x: x[0])
        from collections import deque
        q = deque(intervals)
        while q:
            temp = q.popleft()
            if not res:
                res.append(temp)
            else:
                if res[-1][1] < temp[0]:
                    res.append(temp)
                else:
                    res[-1][1] = max(res[-1][1], temp[1])
        return res