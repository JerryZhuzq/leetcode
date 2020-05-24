class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


a = ListNode(3)
c = ListNode(4)

b = a
b.next = c
print(a.next.val)