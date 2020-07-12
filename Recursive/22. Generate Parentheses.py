class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left_n, right_n = n, n
        res = []
        def helper(l, r, s):
            if r == 0:
                res.append(s)
                return
            if l == r:
                helper(l-1, r, s+'(')
            else:
                if l > 0:
                    helper(l-1, r, s+'(')
                helper(l, r-1, s+')')
        helper(n, n, '')
        return res