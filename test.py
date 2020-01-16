class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones is None or len(stones) == 0:
            return False
        for i in range(1, len(stones) - 1):
            if stones[i] * 2 < stones[i + 1] - stones[i]:
                return False

        pos = [0]
        jumps = [0]
        last_stone = stones[-1]
        stones_set = set(stones)
        while len(pos) > 0:
            p = pos.pop()
            jump = jumps.pop()
            for i in range(jump - 1, jump + 2):
                if i <= 0:
                    continue
                next_pos = p + i
                if next_pos == last_stone:
                    return True
                if next_pos in stones_set:
                    pos.append(next_pos)
                    jumps.append(i)
        return False

    from collections import deque
    if stones[1] != 1:
        return False
    for i in range(1,len(stones)-1):
        if stones[i] *2 < stones[i+1] - stones[i]:
            return False
    stones_Set = set(stones)
    q = deque()
    q.append([1,1])
    while(q):
        temp, step = q.popleft()
        for i in range(max(1, step-1), step+2):
            next_pos = i + temp
            # print(next_pos)
            if next_pos == stones[-1]:
                return True
            if next_pos in stones_Set:
                q.append([next_pos, i])
    return False