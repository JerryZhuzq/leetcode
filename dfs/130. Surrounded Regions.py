class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        visited = set()

        def dfs(m, n, isEscape, tmp):
            visited.add((m, n))
            tmp.append([m, n])
            if not isEscape and (m == 0 or n == 0 or m == len(board) - 1 or n == len(board[0]) - 1) and board[m][
                n] == "O":
                isEscape = True
            if m > 0 and (m - 1, n) not in visited and board[m - 1][n] == "O":
                isEscape, tmp = dfs(m - 1, n, isEscape, tmp)
            if m + 1 < len(board) and (m + 1, n) not in visited and board[m + 1][n] == "O":
                isEscape, tmp = dfs(m + 1, n, isEscape, tmp)
            if n > 0 and (m, n - 1) not in visited and board[m][n - 1] == "O":
                isEscape, tmp = dfs(m, n - 1, isEscape, tmp)
            if n + 1 < len(board[0]) and (m, n + 1) not in visited and board[m][n + 1] == "O":
                isEscape, tmp = dfs(m, n + 1, isEscape, tmp)
            return isEscape, tmp

        for y in range(m):
            for x in range(n):
                if board[y][x] == 'O' and (y, x) not in visited:
                    isEscape, tmp = dfs(y, x, False, [])
                    if not isEscape:
                        for i, j in tmp:
                            board[i][j] = "X"



