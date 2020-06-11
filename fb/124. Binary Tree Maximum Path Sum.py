# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(root, val):
            if not root:
                return min(0, val), min(0, val)
            max_total_l, max_root_l = helper(root.left, root.val)
            max_total_r, max_root_r = helper(root.right, root.val)
            cur_root = max(max_root_l, max_root_r, 0) + root.val
            cur_total = max(max_total_l, max_total_r, cur_root, max_root_l+max_root_r+root.val)
            return cur_total, cur_root
        total, root = helper(root, root.val)
        return total

# The tricky part here is the existence of negative number, which means for non-exist
# node we couldn't just return 0, instead we need to return the number itself or a number less than 0
