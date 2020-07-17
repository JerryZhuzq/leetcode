class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dic = defaultdict(set)
        for u, v in edges:
            # print(u, v)
            if u not in dic[v] and v not in dic[u]:
                dic[v].add(u)
                dic[u].add(v)
                dic[v] = dic[v] | dic[u]
                for x in dic[v]:
                    dic[x] = dic[v]
                for x in dic[u]:
                    dic[x] = dic[v]
                dic[u] = dic[v]
            else:
                return [u, v]
            # print(dic[u], dic[v])
        return []


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [0] * (len(edges) + 1)

        def find_parent(x):
            if parent[x] == 0:
                return x
            parent[x] = find_parent(parent[x])
            return parent[x]

        def union(x, y):
            parent_x = find_parent(x)
            parent_y = find_parent(y)
            if parent_x == parent_y:
                return False
            parent[parent_x] = parent_y
            return True

        for x, y in edges:
            if not union(x, y):
                return [x, y]