class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {k: 0 for k in range(numCourses)}
        pre = defaultdict(list)
        for i, j in prerequisites:
            indegree[i] += 1
            pre[j].append(i)
        res = 0
        dq = deque()
        for i in indegree:
            if indegree[i] == 0:
                dq.append(i)
        while dq:
            cur = dq.popleft()
            res += 1
            for c in pre[cur]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    dq.append(c)
        return res == numCourses