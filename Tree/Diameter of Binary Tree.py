
'''
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''

'''
The kay here is to understand which to return at each node. I choose to return two values, one for
the diameter calculated at the node itself, one for the longest path owned by the node plus one(the path
to parent node). Receiving these two values from left and right child node, the parent node could again
decide to return its own the diameter and the longest path.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def compareDiameterPath(root):
            if not root:
                return 0, 0
            left_diameter, left_path = compareDiameterPath(root.left)
            right_diameter, right_path = compareDiameterPath(root.right)
            return max(left_diameter,right_diameter,left_path+right_path), max(left_path,right_path)+1
        x, y = compareDiameterPath(root)
        return x