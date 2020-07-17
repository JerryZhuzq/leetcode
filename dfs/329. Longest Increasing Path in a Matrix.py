class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        visited = [[0] * n for _ in range(m)]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = 0

        def helper(x, y, val):
            cur_val = val
            for i, j in direction:
                x_i, y_j = x + i, y + j
                if x_i > -1 and x_i < m and y_j > -1 and y_j < n:
                    if matrix[x][y] < matrix[x_i][y_j]:
                        if visited[x_i][y_j] != 0:
                            cur_val = max(cur_val, val + visited[x_i][y_j])
                        else:
                            cur_val = max(cur_val, val + helper(x_i, y_j, val))
            visited[x][y] = cur_val
            return cur_val

        for x in range(m):
            for y in range(n):
                if visited[x][y] != 0:
                    continue
                res = max(res, helper(x, y, 1))
        return res

# dfs with dp, island problem, not hard
