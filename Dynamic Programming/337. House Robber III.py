# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def rob(self, root: TreeNode) -> int:
        def rob_sub(root):
            if not root:
                return [0, 0]
            left_val = rob_sub(root.left)
            right_val = rob_sub(root.right)

            res = [0, 0]
            res[0] = max(left_val[0], left_val[1]) + max(right_val[0], right_val[1])
            res[1] = root.val + left_val[0] + right_val[0]
            return res

        res = rob_sub(root)
        return max(res[0], res[1])







