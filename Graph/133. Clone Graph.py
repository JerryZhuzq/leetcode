"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        from collections import deque
        q = deque()
        store = {}
        new_node = Node(node.val, [])
        q.append((node, new_node))
        store[node.val] = new_node
        while q:
            old, new = q.popleft()
            for n in old.neighbors:
                next_node = None
                if n.val not in store:
                    next_node = Node(n.val, [])
                    q.append((n, next_node))
                    # it shoule be done here otherwise,  the Node
                    # is inconsistent between dict and deque
                    store[n.val] = next_node
                else:
                    next_node = store[n.val]
                new.neighbors.append(next_node)
        return new_node