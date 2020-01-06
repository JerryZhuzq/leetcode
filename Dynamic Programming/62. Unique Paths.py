class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        square = [[0 for i in range(m)] for i in range(n)]
        for i in range(m):
            square[0][i] = 1
        for i in range(n):
            square[i][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                square[i][j] = square[i - 1][j] + square[i][j - 1]
        return square[-1][-1]
