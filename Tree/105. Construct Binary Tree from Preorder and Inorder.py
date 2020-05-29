# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        store = {key: value for value, key in enumerate(inorder)}

        def helper(root, preorder, inorder):
            # print(root.val, preorder, inorder)
            if len(preorder) <= 1:
                return None
            t = store[preorder[0]] - store[inorder[0]]
            # print(t)
            if t == 0:
                root.left = None
                node = TreeNode(preorder[1])
                root.right = node
                helper(node, preorder[1:], inorder[1:])
            elif t == len(preorder) - 1:
                root.right = None
                node = TreeNode(preorder[1])
                root.left = node
                helper(node, preorder[1:t + 1], inorder[:t + 1])
            else:
                left_node = TreeNode(preorder[1])
                root.left = left_node
                right_node = TreeNode(preorder[t + 1])
                root.right = right_node
                helper(left_node, preorder[1:t + 1], inorder[:t])
                helper(right_node, preorder[t + 1:], inorder[t + 1:])

        helper(root, preorder, inorder)

        return root