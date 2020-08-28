class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        store = Counter(words)
        hp = []
        for key in store:
            hp.append([-store[key], key])
        heapq.heapify(hp)
        res = [y for x, y in heapq.nsmallest(k, hp)]
        return res