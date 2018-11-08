
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self):
        self.val = None
        self.next = None


class ListNode_handle:
    def __init__(self):
        self.cur_node = None

    def add(self, lst):
        # add a new node pointed to previous node
        if not lst:
            return None
        node = ListNode()
        node.val = lst[0]
        if len(lst) == 1:
            node.next = None
        else:
            node.next = self.add(lst[1:])
        return node

    def print_ListNode(self, node):
        while node:
            print('\nnode: ', node, ' value: ', node.val, ' next: ', node.next)
            node = node.next

    def _reverse(self, nodelist):
        list = []
        while nodelist:
            list.append(nodelist.val)
            nodelist = nodelist.next
        result = ListNode()
        result_handle = ListNode_handle()
        for i in list:
            result = result_handle.add(i)
        return result

if __name__ == '__main__':
    ListNode_1 = ListNode_handle()
    l1 = ListNode()
    l1_list = [1, 8, 3]
    l1 = ListNode_1.add(l1_list)
    ListNode_1.print_ListNode(l1)