# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList_iterate(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = ListNode(0, head)
        pre = dummy
        cur = head
        while (cur):
            cur.next, cur, pre = pre, cur.next, cur
        head.next = None
        return pre

    def reverseList_recursive(self, head: ListNode) -> ListNode:
        if not head:
            return None

        def helper(node, pre):
            if not node:
                return pre
            res = helper(node.next, node)
            node.next = pre
            return res

        return helper(head, None)
