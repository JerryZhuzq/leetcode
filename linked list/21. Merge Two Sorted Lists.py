# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        import sys
        dummy = ListNode(-sys.maxsize)
        pre = None
        pre = dummy
        while (l1 and l2):
            if l1.val <= l2.val:
                pre.next, pre, l1 = l1, l1, l1.next
            else:
                pre.next, pre, l2 = l2, l2, l2.next
        if not l1:
            pre.next = l2
        elif not l2:
            pre.next = l1
        return dummy.next



# remember to create a dummy node which could reduce the complexity of such problems
