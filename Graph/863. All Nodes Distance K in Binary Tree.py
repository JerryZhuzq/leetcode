# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        store = defaultdict(list)
        def helper(root, parent):
            if not root:
                return
            if parent:
                store[root.val].append(parent.val)
            if root.left:
                store[root.val].append(root.left.val)
                helper(root.left, root)
            if root.right:
                store[root.val].append(root.right.val)
                helper(root.right, root)
        helper(root, None)
        res = []
        def bfs(root, parent, cur_k):
            nonlocal res
            if cur_k == K:
                res.append(root)
                return
            for i in store[root]:
                if i != parent:
                    bfs(i, root, cur_k+1)
        bfs(target.val, None, 0)
        return res