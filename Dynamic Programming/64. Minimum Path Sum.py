class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if col == 0 or row == 0:
                    if col == 0 and row == 0:
                        continue
                    elif row == 0:
                        grid[row][col] += grid[row][col - 1]
                    elif col == 0:
                        grid[row][col] += grid[row - 1][col]
                else:
                    grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
        return grid[-1][-1]
