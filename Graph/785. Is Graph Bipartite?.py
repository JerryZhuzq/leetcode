# dfs with color node

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = defaultdict(int)
        for i in range(len(graph)):
            if i not in visited:
                stack = deque(graph[i])
                visited[i] = 1
                while stack:
                    n = stack.pop()
                    for nn in graph[n]:
                        if nn not in visited:
                            visited[nn] = abs(visited[n] - 1)
                            stack.append(nn)
                        elif visited[nn] == visited[n]:
                            return False
        return True
