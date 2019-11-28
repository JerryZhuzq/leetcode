class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        grid_y, grid_x = len(grid), len(grid[0])
        res = 0
        visited = set()
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(grid, x, y):
            visited.add((y, x))
            for m in direction:
                newx = x + m[0]
                newy = y + m[1]
                if -1 < newy < grid_y and -1 < newx < grid_x and int(grid[newy][newx]) == 1 and (
                newy, newx) not in visited:
                    dfs(grid, newx, newy)
            return

        for i in range(grid_y):
            for j in range(grid_x):
                # print(i,j, grid[i][j],visited)
                if int(grid[i][j]) == 1 and (i, j) not in visited:
                    # print(res)
                    dfs(grid, j, i)
                    res += 1

        return res