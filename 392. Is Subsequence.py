class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = 0
        if not s:
            return True
        if not t:
            return False
        for i in t:
            if s[n] == i:
                n += 1
                if n == len(s):
                    return True
        return False

