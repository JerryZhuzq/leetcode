"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        if head == None:
            return None
        node_dict = {}
        cur_node = head
        n = 0
        while cur_node:
            node_dict[cur_node] = n
            cur_node = cur_node.next
            n += 1
        store = []
        cur_node = head
        while cur_node:
            if cur_node.random == None:
                cur_node = cur_node.next
                store.append(None)
                continue
            store.append(node_dict[cur_node.random])
            cur_node = cur_node.next

        cur = head
        pre = Node(0, None, None)
        cur_store = []

        while cur:
            new_cur = Node(cur.val, None, None)
            cur_store.append(new_cur)
            pre.next, pre, cur = new_cur, new_cur, cur.next

        for i, node in enumerate(cur_store):
            if store[i] == None:
                node.random = None
            else:
                node.random = cur_store[store[i]]
        return cur_store[0]

# Python 2 version


# if(head == null) return head;
#         Map<Node,Node> map = new HashMap();
#         Node temp = head;
#         while(temp != null){
#             map.put(temp,new Node(temp.val)); //creating a dummy node for every node with same value and putting
#             temp = temp.next;                  //in map against that node
#         }
#         temp = head;//again start with head and set next and random links
#         while(temp != null){
#             map.get(temp).next = map.get(temp.next);//dummy nodes in map's value need to be given links for
#             map.get(temp).random = map.get(temp.random);//next & random pointers and their next and random
#             temp = temp.next;     //should next and random of original list
#         }
#         return map.get(head);

# Java version


