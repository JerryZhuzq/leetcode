# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         import sys
#         dummy = ListNode(sys.maxsize)
#         pre = dummy
#         k = len(lists)
#         count_none = 0
#         min_index = 0
#         while(count_none < k):
#             cur_none = 0
#             cur_min = sys.maxsize
#             for i in range(len(lists)):
#                 if not lists[i]:
#                     cur_none += 1
#                 elif lists[i].val < cur_min:
#                     cur_min = lists[i].val
#                     min_index = i
#             count_none = cur_none
#             if count_none == k:
#                 break
#             pre.next, pre, lists[min_index] = lists[min_index], lists[min_index], lists[min_index].next
#         return dummy.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        from queue import PriorityQueue
        q = PriorityQueue()
        count = 0
        for node in lists:
            if node:
                q.put((node.val, count, node))
                count += 1
        dummy = ListNode(0)
        cur = dummy
        while(not q.empty()):
            temp_val, count, temp_node = q.get()
            node = ListNode(temp_val)
            cur.next, cur = node, node
            print(cur.next, cur)
            input()
            temp_node = temp_node.next
            if temp_node:
                q.put((temp_node.val, count, temp_node))
        return dummy.next


def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    import heapq
    q = []
    count = 0
    dummy = ListNode(0)
    pre = dummy
    for node in lists:
        if node:
            heappush(q, (node.val, count, node))
        count += 1
    while (q):
        val, count, node = heappop(q)
        temp = ListNode(val)
        pre.next, pre = temp, temp
        node = node.next
        if node:
            heappush(q, (node.val, count, node))
    return dummy.next

# multiple linked list could be solved using this method.
# push each linked not into priority queue to heapify to achieve
# sorted lists
