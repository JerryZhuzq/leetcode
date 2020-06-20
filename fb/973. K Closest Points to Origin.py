class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import heapq
        return heapq.nsmallest(K, points, key=lambda x: x[0]**2+x[1]**2)