class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        isPac = set()
        isAtl = set()
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def inArea(x, y, newx, newy):
            if (newx < 0 or newy < 0 or newx > n - 1 or newy > m - 1) or matrix[newy][newx] < matrix[y][x]:
                return False
            return True

        def dfs(x, y, visited):
            if (y, x) in visited:
                return
            visited.add((y, x))
            for pos in direction:
                newx = x + pos[1]
                newy = y + pos[0]
                if inArea(x, y, newx, newy):
                    dfs(newx, newy, visited)

        for y in range(m):
            dfs(0, y, isPac)
            dfs(n - 1, y, isAtl)
        for x in range(n):
            dfs(x, 0, isPac)
            dfs(x, m - 1, isAtl)
        return list(isPac & isAtl)