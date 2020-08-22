# BFS with coloring

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if N == 1:
            return True
        relation = defaultdict(list)
        for x, y in dislikes:
            relation[x].append(y)
            relation[y].append(x)
        color = {}
        for x, y in dislikes:
            if x not in color:
                color[x] = 0
                q = deque()
                q.append(x)
                while q:
                    cur_node = q.popleft()
                    for n in relation[cur_node]:
                        if n in color:
                            if color[n] == color[cur_node]:
                                return False
                        else:
                            color[n] = abs(color[cur_node] - 1)
                            q.append(n)
        return True
