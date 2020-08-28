class DoubleLinkedList:
    def __init__(self, key, value):
        self.value = [key, value]
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):

        head = DoubleLinkedList(0, 0)
        self.head = head
        tail = DoubleLinkedList(0, 0)
        self.tail = tail
        self.head.next, self.tail.pre = self.tail, self.head
        self.store = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.store:
            self.store[key].pre.next, self.store[key].next.pre = self.store[key].next, self.store[key].pre
            self.tail.pre.next, self.tail.pre, self.store[key].pre, self.store[key].next = self.store[key], self.store[
                key], self.tail.pre, self.tail
            return self.store[key].value[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key].pre.next, self.store[key].next.pre = self.store[key].next, self.store[key].pre
            self.tail.pre.next, self.tail.pre, self.store[key].pre, self.store[key].next = self.store[key], self.store[key], self.tail.pre, self.tail
            self.store[key].value[1] = value
        else:
            new_key = DoubleLinkedList(key, value)
            if len(self.store) == self.capacity:
                self.store.pop(self.head.next.value[0])
                self.head.next.next.pre, self.head.next.pre, self.head.next.next, self.head.next = self.head, None, None, self.head.next.next
            self.store[key] = new_key
            self.tail.pre.next, self.tail.pre, new_key.pre, new_key.next = new_key, new_key, self.tail.pre, self.tail
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# The trick lies at using double linked list + Hashmap to store each pair of key and value

class LRUCache:

    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.d = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            self.d.move_to_end(key)
            return self.d[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.move_to_end(key)
        elif len(self.d) == self.capacity:
            self.d.popitem(last=False)
        self.d[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)