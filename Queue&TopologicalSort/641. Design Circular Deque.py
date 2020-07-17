class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.maxlength = k
        self.deque = [None] * 2 * k
        self.left = k // 2 + 1
        self.right = k // 2

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.right - self.left < self.maxlength - 1:
            if self.left == 0:
                newblock = [None] * len(self.deque)
                self.deuqe = newblock + self.deque
            self.left -= 1
            self.deque[self.left] = value
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.right - self.left < self.maxlength - 1:
            if self.right == len(self.deque) - 1:
                newblock = [None] * len(self.deque)
                self.deque = self.deque + newblock
            self.right += 1
            self.deque[self.right] = value
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.deque[self.left] = None
        self.left += 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.deque[self.right] = None
        self.right -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.deque[self.left] if self.deque[self.left] != None else -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.deque[self.right] if self.deque[self.right] != None else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.left == self.right + 1

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.right - self.left == self.maxlength - 1

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


# Create a fixed size list and append element from the middle