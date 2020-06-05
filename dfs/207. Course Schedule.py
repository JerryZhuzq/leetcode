class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        visited = set()
        if numCourses == 1:
            return True
        pre_dict = {}
        for pre in prerequisites:
            pre_dict[pre[0]] = pre_dict.get(pre[0], []) + [pre[1]]

        def dfs(node, cur_visited):
            if node in visited:
                return True
            if node not in pre_dict:
                visited.add(node)
                return True
            visited.add(node)
            cur_visited.add(node)
            for child in pre_dict[node]:
                if child in cur_visited:
                    # print(node, child, cur_visited, visited, 111)
                    return False
                elif not dfs(child, cur_visited):
                    # print(node, child, cur_visited, visited, 222)
                    return False
                if child in cur_visited:
                    cur_visited.remove(child)
            return True

        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        return True

# time complexity O(V+E)  graph depth first search
