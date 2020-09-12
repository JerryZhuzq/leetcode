class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        res = set()
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(i, j, island, l, r):
            if grid[i][j] == 0:
                return island
            grid[i][j] = 0
            island.append((i - l, j - r))
            for a, b in direction:
                x, y = a + i, b + j
                if x > -1 and x < len(grid) and y > -1 and y < len(grid[0]):
                    island = dfs(x, y, island, l, r)
            return island

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cur_island = dfs(i, j, [], i, j)
                    res.add(tuple(cur_island))
        return len(res)