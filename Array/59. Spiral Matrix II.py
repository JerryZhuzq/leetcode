class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]

        row_t = col_l = 0
        row_b = col_r = n - 1

        cur = 1
        while row_t <= row_b and col_l <= col_r:
            for i in range(col_l, col_r + 1):
                res[row_t][i] = cur
                cur += 1
            row_t += 1
            for i in range(row_t, row_b + 1):
                res[i][col_r] = cur
                cur += 1
            col_r -= 1

            if row_t <= row_b:
                for i in range(col_r, col_l - 1, -1):
                    res[row_b][i] = cur
                    cur += 1
                row_b -= 1
            if col_l <= col_r:
                for i in range(row_b, row_t - 1, -1):
                    res[i][col_l] = cur
                    cur += 1
                col_l += 1
        return res


