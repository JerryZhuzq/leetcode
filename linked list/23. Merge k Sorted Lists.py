# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import sys
        dummy = ListNode(sys.maxsize)
        pre = dummy
        k = len(lists)
        count_none = 0
        min_index = 0
        while(count_none < k):
            cur_none = 0
            cur_min = sys.maxsize
            for i in range(len(lists)):
                if not lists[i]:
                    cur_none += 1
                elif lists[i].val < cur_min:
                    cur_min = lists[i].val
                    min_index = i
            count_none = cur_none
            if count_none == k:
                break
            pre.next, pre, lists[min_index] = lists[min_index], lists[min_index], lists[min_index].next
        return dummy.next