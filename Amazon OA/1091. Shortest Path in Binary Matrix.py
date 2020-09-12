class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        grid[0][0] = 1
        q = deque()
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]
        q.append((0, 0, 1))
        while q:
            i, j, l = q.popleft()
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return l
            l += 1
            for a, b in direction:
                x, y = i+a, j+b
                if x > -1 and x < len(grid) and y > -1 and y < len(grid[0]) and grid[x][y] != 1:
                    grid[x][y] = 1
                    q.append((x, y, l))
        return -1