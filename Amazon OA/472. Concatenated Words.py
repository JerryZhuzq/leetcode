class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, s):
        trie = self.trie
        for ss in s:
            if ss not in trie:
                trie[ss] = {}
            trie = trie[ss]
        trie['#'] = 1


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()
        res = []
        for w in words:
            trie.insert(w)

        # print(trie.trie)
        def dfs(start, count, root, word):
            cur_root = root
            for i in range(start, len(word)):
                if word[i] not in cur_root:
                    return False
                cur_root = cur_root[word[i]]
                if '#' in cur_root:
                    if i == len(word) - 1:
                        return count >= 1
                    elif dfs(i + 1, count + 1, root, word):
                        return True
            return False

        for w in words:
            if dfs(0, 0, trie.trie, w):
                res.append(w)
        return res


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set()
        words.sort(key=lambda x: len(x))
        res = []

        def helper(word):
            if word in word_set:
                return True
            for i in range(len(word)):
                if word[:i + 1] in word_set and helper(word[i + 1:]):
                    return True
            return False

        for word in words:
            if helper(word):
                res.append(res)
            word_set.add(word)
        return res



