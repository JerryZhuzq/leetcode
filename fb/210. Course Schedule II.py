class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_dict = {i: [] for i in range(numCourses)}
        for cour, pre in prerequisites:
            course_dict[cour] += [pre]
        visited = set()
        res = []

        def dfs(i, pre_temp):
            if i in visited:
                return 0
            if i in pre_temp:
                return -1
            if not course_dict[i]:
                res.append(i)
                visited.add(i)
                return 0
            pre_temp.add(i)
            for pre in course_dict[i]:
                if dfs(pre, pre_temp) == -1:
                    return -1
            res.append(i)
            visited.add(i)
            pre_temp.remove(i)
            return 0

        for i in range(numCourses):
            if i not in visited:
                if dfs(i, set()) == -1:
                    return []
        return res

# dfs try to memorize the node being visited
