class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_values = [float("-inf")]

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x >= self.max_values[-1]:
            self.max_values.append(x)

    def pop(self) -> int:
        if self.stack[-1] == self.max_values[-1]:
            self.max_values.pop()

        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_values[-1]

    def popMax(self) -> int:
        res = self.max_values.pop()
        tmp = []
        while self.stack:
            if self.stack[-1] == res:
                self.stack.pop()
                break
            tmp.append(self.stack.pop())
        while tmp:
            self.push(tmp.pop())
        return res

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()