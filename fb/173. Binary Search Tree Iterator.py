# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        from collections import deque
        self.seq = deque()

        def helper(root):
            if not root:
                return
            helper(root.left)
            self.seq.append(root.val)
            helper(root.right)

        helper(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext:
            return self.seq.popleft()
        else:
            return null

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.seq:
            return True
        else:
            return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()