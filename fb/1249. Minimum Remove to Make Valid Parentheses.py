class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        temp = []
        left_parenthese = 0
        from collections import Counter
        l, r = Counter(s)['('], Counter(s)[')']
        for i in s:
            if i == '(':
                if left_parenthese < r:
                    temp.append(i)
                    left_parenthese += 1
            elif i ==')':
                r -= 1
                if left_parenthese > 0:
                    temp.append(i)
                    left_parenthese -= 1
            else:
                temp.append(i)
        return ''.join(temp)

# Firstly count the number of both parentheses, and decide whether to append
# parentheses according to number of current ( and incoming )

