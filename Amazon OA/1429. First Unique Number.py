class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = OrderedDict()
        self.visited = set()
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        for num in self.queue.keys():
            return num
        return -1

    def add(self, value: int) -> None:
        if value not in self.visited:
            self.queue[value] = 1
            self.visited.add(value)
        else:
            if value in self.queue:
                self.queue.pop(value)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)