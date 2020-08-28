class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lfu = defaultdict(OrderedDict)
        self.least = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            least = self.cache[key][1]
            value = self.cache[key][0]
            self.cache[key][1] += 1
            self.lfu[least].pop(key)
            self.lfu[least + 1][key] = value
            if self.least == least and len(self.lfu[least]) == 0:
                self.least += 1

            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key][0] = value
            least = self.cache[key][1]
            self.cache[key][1] += 1
            self.lfu[least].pop(key)
            self.lfu[least + 1][key] = value
            if self.least == least and len(self.lfu[least]) == 0:
                self.least += 1
        else:
            if len(self.cache) == self.capacity:
                if self.capacity == 0:
                    return
                least = self.least
                pop_key, pop_value = self.lfu[least].popitem(last=False)
                self.cache.pop(pop_key)
            self.cache[key] = [value, 1]
            self.least = 1
            self.lfu[1][key] = value
        # print(self.lfu)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
#
# Use two dictionaries, a cache to store the value as well as the frequency, another lfu dictionary to store multiple
# ordered dictionaries