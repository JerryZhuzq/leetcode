class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        left_brackt = []
        for i in s:
            if i == ')':
                left_index = left_brackt.pop()
                stack = stack[:left_index] + stack[left_index:][::-1]
            elif i == '(':
                left_brackt.append(len(stack))
            else:
                stack.append(i)
        return ''.join(stack)

# time complexity: O(n^2)



# wormholes solution time complexity:O(n)

class Solution:
    def reverseParentheses(self, s: str) -> str:
        left_bracket = []
        pair = {}
        for i, n in enumerate(s):
            if n == '(':
                left_bracket.append(i)
            elif n == ')':
                j = left_bracket.pop()
                pair[i], pair[j] = j, i
        res = []
        i = 0
        d = 1
        while i < len(s):
            if s[i] in '()':
                i = pair[i]
                d = -d
            else:
                res.append(s[i])
            i += d
        return ''.join(res)
