class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        trie = self.trie
        for s in word:
            if s not in trie:
                trie[s] = {}
            trie = trie[s]
        trie['#'] = 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        res = []
        for word in words:
            trie.insert(word)

        def dfs(i, j, cur, node):
            # put at the front is because the key '#' is a value of the last letter
            if '#' in node:
                res.append(cur)
                node.pop('#')
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
                return
            if board[i][j] not in node:
                return
            tmp, board[i][j] = board[i][j], '$'
            dfs(i + 1, j, cur + tmp, node[tmp])
            dfs(i - 1, j, cur + tmp, node[tmp])
            dfs(i, j + 1, cur + tmp, node[tmp])
            dfs(i, j - 1, cur + tmp, node[tmp])
            board[i][j] = tmp

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, '', trie.trie)
        return res





