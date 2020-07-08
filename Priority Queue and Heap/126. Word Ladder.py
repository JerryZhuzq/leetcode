class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        import collections
        import sys
        bfs = collections.deque()
        least = sys.maxsize
        s = set()
        cur_s = set()
        cur_s.add(beginWord)
        cur_step = 0
        bfs.append([[beginWord], 1])
        store = collections.defaultdict()
        res = []

        def transformation(word):
            for i in range(len(word)):
                yield word[:i] + '*' + word[i + 1:]

        for word in wordList:
            for i in transformation(word):
                store[i] = store.get(i, []) + [word]
        while (bfs):
            cur_list, step = bfs.popleft()
            if step > least:
                continue
            if step > cur_step:
                cur_step = step
                s = s | cur_s
                cur_s.clear()
            for i in transformation(cur_list[-1]):
                if i in store:
                    for word in store[i]:
                        if word in s:
                            continue
                        if word == endWord and step < least:
                            least = step + 1
                            res.append(cur_list + [word])
                            break
                        else:
                            cur_s.add(word)
                            bfs.append([cur_list + [word], step + 1])
        return res