'''

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.



MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

'''


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack = []
        self.minstore = []

    def push(self, x: int) -> None:
        self.minstack.append(x)
        heappush(self.minstore, x)   #Use a heap to manage the minimum elements

    def pop(self) -> None:
        if self.minstack:
            val = self.minstack[-1]
            self.minstack.pop()
            self.minstore.remove(val)
            self.minstore.sort()

    def top(self) -> int:
        if self.minstack:
            return self.minstack[-1]

    def getMin(self) -> int:
        if self.minstore:
            return self.minstore[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()