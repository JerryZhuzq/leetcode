# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        first_root = TreeNode(postorder[-1])
        instore = {key: value for value, key in enumerate(inorder)}
        poststore = {key: value for value, key in enumerate(postorder)}
        def helper(root, inorder, postorder):
            if len(inorder) == 1:
                return TreeNode(inorder[0])
            t = instore[root.val] - instore[inorder[0]]
            if t == 0:
                root_right = TreeNode(postorder[-2])
                root.right = helper(root_right,inorder[1:], postorder[:-1])
            elif t == len(inorder)-1:
                root_left = TreeNode(postorder[t-1])
                root.left = helper(root_left, inorder[:t], postorder[:t])
            else:
                root_left = TreeNode(postorder[t-1])
                root.left = helper(root_left, inorder[:t], postorder[:t])
                root_right = TreeNode(postorder[-2])
                root.right = helper(root_right, inorder[t+1:], postorder[t:-1])
            return root
        return helper(first_root, inorder, postorder)


# find the root index relation between inorder and postorder
# the postorder[-1] is always the root,
# postorder[-2] is the root of right sub tree
# postorder[inorder.index(postorder[-1])-1] is the root of left sub tree
