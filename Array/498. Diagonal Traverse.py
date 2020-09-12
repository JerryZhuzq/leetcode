class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        different = 1
        res = []
        for i in range(m+n-1):
            tmp = []
            for j in range(max(0, i-(m-1)), min(i+1, n)):
                tmp.append(matrix[i-j][j])
            if different == 1:
                res += tmp
            else:
                res += tmp[::-1]
            different = -different
        return res


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        store = defaultdict(list)
        res = []
        for i in range(m):
            for j in range(n):
                store[i+j].append(matrix[i][j])
        for i in range(m+n-1):
            if i % 2 == 0:
                res += store[i][::-1]
            else:
                res += store[i]
        return res