class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        res = [[0, 0]]
        hp = [(0, maxsize)]
        events = sorted([(l, -h, r) for l, r, h in buildings] + list({(r, 0, 0) for l, r, h in buildings}))

        for l, h, r in events:

            while l >= hp[0][1]:
                heapq.heappop(hp)

            if h:
                heapq.heappush(hp, (h, r))

            if hp[0][0] != -res[-1][1]:
                res.append([l, -hp[0][0]])
        return res[1:]