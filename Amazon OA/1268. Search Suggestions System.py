# faster solution

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(searchWord)
        res = [[] for _ in range(n)]

        for p in products:
            i = 0
            while i < n and i < len(p) and p[:i + 1] == searchWord[:i + 1]:
                res[i].append(p)
                i += 1
        for i in range(n):
            res[i].sort()
            res[i] = res[i][:3]
        return res


# slower solution

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(searchWord)
        res = []
        for i in range(1, n+1):
            h = []
            for p in products:
                if p.startswith(searchWord[:i]):
                    heapq.heappush(h, p)
            res.append(heapq.nsmallest(3, h))
        return res