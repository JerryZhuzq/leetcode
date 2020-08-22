class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        store = defaultdict(list)
        for x, y in connections:
            store[x].append(y)
            store[y].append(x)

        visited = defaultdict()
        res = []

        def dfs(node, time, parent):
            if node not in visited:
                visited[node] = time
                expected_time = time + 1
                for i in store[node]:
                    if i != parent:
                        actual_time = dfs(i, expected_time, node)
                        if actual_time >= expected_time:
                            res.append([node, i])
                        visited[node] = min(visited[node], actual_time)
            return visited[node]

        dfs(0, 0, -1)

        return res