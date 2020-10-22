class Trie:
    def __init__(self):
        self.trie = {}
        self.trie['last'] = 0

    def insert(self, word, seq):
        trie = self.trie
        for s in word:
            if s not in trie:
                trie['last'] = seq
                trie[s] = {}
            trie = trie[s]
            trie['last'] = seq

    def search(self, word):
        trie = self.trie
        for s in word:
            if s not in trie:
                return trie['last']
            trie = trie[s]
        return trie['last']


def binary_complete(command):
    trie = Trie()

    res = []
    for i, c in enumerate(command):
        r = trie.search(c)
        trie.insert(c, i+1)
        res.append(r)
    # print(trie.trie)
    return res


print(binary_complete(['000', '1110', '01', '001', '110', '11']))
print(binary_complete(['100110', '1001', '1001111']))
print(binary_complete(['1', '10', '11010']))
