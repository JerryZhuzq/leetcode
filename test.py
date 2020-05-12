class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


dummy = ListNode(0)
head = ListNode(2)

pre = head
pre = dummy

print(pre.val)