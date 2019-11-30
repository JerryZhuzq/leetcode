class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:
            return []
        res = []
        col = [False for x in range(n)]
        dia1 = [False for x in range(2 * n - 1)]
        dia2 = [False for x in range(2 * n - 1)]

        def genAns(n, row):
            ans = []
            for i in range(n):
                tmp = ""
                for j in range(n):
                    if j == row[i]:
                        tmp += "Q"
                    else:
                        tmp += "."
                ans.append(tmp)
            return ans

        def putNQueens(n, index, row):  # index stands for the index number of row
            if index == n:
                res.append(genAns(n, row))
                return
            for i in range(n):  # i stands for the index number of column
                if (col[i] != True and dia1[index + i] != True and dia2[index - i + n - 1] != True):
                    col[i] = True
                    dia1[index + i] = True
                    dia2[index - i + n - 1] = True
                    putNQueens(n, index + 1, row + [i])
                    col[i] = False
                    dia1[index + i] = False
                    dia2[index - i + n - 1] = False

        putNQueens(n, 0, [])
        return res