# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def helper(start, end):
            if start > end:
                return [None, ]  # need to be checked

            res = []
            for i in range(start, end + 1):
                left_nodes = helper(start, i - 1)
                right_nodes = helper(i + 1, end)

                for l in left_nodes:
                    for r in right_nodes:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res

        return helper(1, n) if n > 0 else []
