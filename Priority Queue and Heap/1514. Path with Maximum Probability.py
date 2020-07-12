import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        score, edges_d, dist = {}, defaultdict(list), {}
        for i in range(len(edges)):
            x, y = edges[i]
            score[(x,y)] = succProb[i]
            score[(y,x)] = succProb[i]
            edges_d[x].append(y)
            edges_d[y].append(x)
        q = []
        dist[0] = 1
        for e in edges_d[start]:
            dist[e] = score[(start, e)]
            heapq.heappush(q, [-dist[e], e])
        while q:
            val, node = heapq.heappop(q)
            val = - val
            if node == end:
                return val
            for adj in edges_d[node]:
                if adj not in dist:
                    dist[adj] = val*score[(node, adj)]
                    heapq.heappush(q, [-dist[adj], adj])
                else:
                    temp = val*score[(node, adj)]
                    if temp > dist[adj]:
                        dist[adj] = temp
                        heapq.heappush(q, [-dist[adj], adj])
        return 0

# dijkstra algorithm. Build a dict to memorize the distance between current visited
# node and node for the next step. After visiting the node with maximum possibility,
# we compute its neighbors' possibility and compare them with validate value in
# distance dict and choose the higher one
