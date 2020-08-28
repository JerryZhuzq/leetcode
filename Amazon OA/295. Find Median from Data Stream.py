class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.median = None
        self.left_heap = []
        self.right_heap = []
        self.total_length = 0

    def addNum(self, num: int) -> None:
        self.total_length += 1
        if self.median is None:
            self.median = num
            return

        if num >= self.median:
            if len(self.left_heap) == len(self.right_heap) - 1:
                heapq.heappush(self.left_heap, -self.median)
                self.median = heapq.heappushpop(self.right_heap, num)
            else:
                heapq.heappush(self.right_heap, num)
        else:
            if len(self.left_heap) == len(self.right_heap):
                heapq.heappush(self.right_heap, self.median)
                self.median = -heapq.heappushpop(self.left_heap, -num)
            else:
                heapq.heappush(self.left_heap, -num)

    def findMedian(self) -> float:
        if self.median is None:
            return 0
        if self.total_length % 2 == 0:
            return (self.median + self.right_heap[0]) / 2
        return float(self.median)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()