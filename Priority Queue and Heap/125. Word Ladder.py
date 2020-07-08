class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        import collections
        q = collections.deque()
        storage = collections.defaultdict()
        visited = set()
        q.append((beginWord, 1))

        def transformation(word):
            for i in range(len(word)):
                yield word[:i] + '*' + word[i + 1:]

        for word in wordList:
            for i in transformation(word):
                storage[i] = storage.get(i, []) + [word]

        while (q):
            cur_word, cur_step = q.popleft()
            for i in transformation(cur_word):
                if i in storage:
                    # visited.add(i)
                    for word in storage[i]:
                        if word == endWord:
                            return cur_step + 1
                        if word not in visited:
                            visited.add(word)
                            q.append((word, cur_step + 1))
        return 0