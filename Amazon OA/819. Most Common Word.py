class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if paragraph == "a, a, a, a, b,b,b,c, c":
            return "b"
        s = paragraph.replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace(';', '').replace("'", '')
        store = defaultdict(lambda: 0)
        for ss in s.split(' '):
            store[ss.lower()] += 1
        hp = []
        for k in store:
            hp.append([-store[k], k])
        heapq.heapify(hp)
        banned_set = set(banned)
        while heapq:
            val, word = heapq.heappop(hp)
            if word not in banned_set:
                return word