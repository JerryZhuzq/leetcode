def wordBreak(s: str, wordDict):
    def helper(i):
        if i == len(s):
            return [[]]

        temp = []
        for word in wordDict:
            if s.startswith(word, i):
                for words in helper(i + len(word)):
                    temp.append([word] + words)
        return temp
    return [' '.join(x) for x in helper(0)]



print(wordBreak(s, wordDict))