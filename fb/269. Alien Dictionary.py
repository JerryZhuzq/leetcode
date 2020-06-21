class Solution:
    def alienOrder(self, words: List[str]) -> str:
        res = []
        indegree = dict(zip(set(''.join(words)), [0] * len(set(''.join(words)))))
        adjacent = dict(zip(set(''.join(words)), [[] for _ in range(len(set(''.join(words))))]))
        total_length = len(indegree)
        pre_word = words[0]
        for word in words[1:]:
            for c in range(len(word)):
                if c == len(pre_word):
                    break
                if word[c] != pre_word[c]:
                    indegree[word[c]] += 1
                    adjacent[pre_word[c]].append(word[c])
                    break
            if word == pre_word[:len(word)] and word != pre_word:
                return ""
            pre_word = word
        from collections import deque
        q = deque()
        for word in indegree:
            if indegree[word] == 0:
                q.append(word)
        while q:
            cur = q.popleft()
            res.append(cur)
            if adjacent[cur]:
                for word in adjacent[cur]:
                    indegree[word] -= 1
                    if indegree[word] == 0:
                        q.append(word)
        ans = ''.join(res)
        if len(res) < total_length:
            return ""
        else:
            return ans
