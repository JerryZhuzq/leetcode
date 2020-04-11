class Solution:
    def canCross(self, stones: List[int]) -> bool:
        from collections import deque
        if stones[1] != 1:
            return False
        for i in range(1, len(stones) - 1):
            if stones[i] * 2 < stones[i + 1] - stones[i]:
                return False
        stones_Set = set(stones)
        q = deque()
        q.append([0, 0])
        while (q):
            temp, step = q.pop()
            for i in range(max(1, step - 1), step + 2):
                next_pos = i + temp
                if next_pos == stones[-1]:
                    return True
                if next_pos in stones_Set:
                    q.append([next_pos, i])
        return False
