class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_set = set()
        rotten = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_set.add((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j, 0))
        res = 0
        while rotten:
            i, j, res = rotten.popleft()
            for x, y in [[0,1], [0, -1], [1, 0], [-1, 0]]:
                next_x, next_y = i+x, j+y
                if next_x > -1 and next_x < len(grid) and next_y > -1 and next_y < len(grid[0]) and (next_x, next_y) in fresh_set:
                    rotten.append((next_x, next_y, res+1))
                    fresh_set.remove((next_x, next_y))
        return res if len(fresh_set) == 0 else -1