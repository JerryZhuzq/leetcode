# Union-find
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)

        index = [i for i in range(n)]

        def find(i):
            while i != index[i]:
                i = index[i]
            return i

        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    index[find(i)] = find(j)
        for i in range(n):
            index[i] = find(i)

        return len(set(index))

# dfs

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        connected = defaultdict(list)
        visited = set()
        res = 0

        for i in range(n):
            for j in range(n):
                if M[i][j] == 1 and i != j:
                    connected[i].append(j)

        for i in range(n):
            if i not in visited:
                res += 1
                visited.add(i)
                dq = deque(connected[i])
                while dq:
                    node = dq.pop()
                    if node not in visited:
                        visited.add(node)
                        dq += connected[node]
        return res
