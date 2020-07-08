from heapq import heappush
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        import heapq
        m = len(heightMap)
        n = len(heightMap[0])
        direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visited = set()
        h = []
        res = 0
        for i in [0, m - 1]:
            for j in range(n):
                visited.add((i, j))
                heappush(h, [heightMap[i][j], i, j])

        for j in [0, n - 1]:
            for i in range(m):
                visited.add((i, j))
                heappush(h, [heightMap[i][j], i, j])

        while h:
            cur_val, i, j = heapq.heappop(h)
            for x, y in direction:
                i_x, j_y = i + x, j + y
                if i_x < 0 or i_x > m - 1 or j_y < 0 or j_y > n - 1:
                    continue
                if (i_x, j_y) not in visited:
                    visited.add((i_x, j_y))
                    if heightMap[i_x][j_y] < cur_val:
                        res += cur_val - heightMap[i_x][j_y]
                        heappush(h, [cur_val, i_x, j_y])
                    else:
                        heappush(h, [heightMap[i_x][j_y], i_x, j_y])
        return res

# the key here is to create a heap to pop the lowest bar between all current
# processed bars in order to get the real trapping water
