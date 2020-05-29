# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        def helper(root):
            if not root:
                return
            left_tail = helper(root.left)
            right_tail = helper(root.right)
            if not left_tail and not right_tail:
                return root
            if not left_tail and right_tail:
                return right_tail
            if left_tail and not right_tail:
                root.left, root.right = None, root.left
                return left_tail
            if left_tail and right_tail:
                left_tail.right, root.right, root.right, root.left = root.right, None, root.left, None
                return right_tail
        helper(root)


# The trick here is to return the tail of each recursive call in order to offer tails for the next flattens
# 把每次递归调用的尾部节点返回，再上一级中可以作为衔接节点，注意树的节点操作，添加子节点也要删除子节点
