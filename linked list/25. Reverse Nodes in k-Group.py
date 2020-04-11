# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k <= 1:
            return head
        count = 0
        cur_node = head
        while (cur_node):
            count += 1
            cur_node = cur_node.next
        divide_times = count // k
        if divide_times < 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        cur_head = head
        pre_head = dummy
        for i in range(divide_times):
            if i == 0:
                for j in range(k):
                    pre, cur.next, cur = cur, pre, cur.next
                head = pre
                pre_head = cur_head
                pre, cur_head.next, cur_head = cur_head, cur, cur
            else:
                for j in range(k):
                    pre, cur.next, cur = cur, pre, cur.next
                pre_head.next, pre_head = pre, cur_head
                pre, cur_head.next, cur_head = cur_head, cur, cur
        return head


