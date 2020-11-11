class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        grid = {}
        for i in range(3):
            for j in range(3):
                grid[(i, j)] = set()

        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    grid[(i // 3, j // 3)].add(board[i][j])

        def dfs(x, y):
            if x == 9:
                return True
            if board[x][y] == '.':
                for k in range(1, 10):
                    if str(k) not in row[x] and str(k) not in col[y] and str(k) not in grid[(x // 3, y // 3)]:
                        board[x][y] = str(k)
                        row[x].add(str(k))
                        col[y].add(str(k))
                        grid[(x // 3, y // 3)].add(str(k))
                        if dfs(x + y // 8, (y + 1) % 9):
                            return True
                        board[x][y] = "."
                        row[x].remove(str(k))
                        col[y].remove(str(k))
                        grid[(x // 3, y // 3)].remove(str(k))
            else:
                if dfs(x + y // 8, (y + 1) % 9):
                    return True

        dfs(0, 0)






