class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        l = len(s)
        for i in range(l):
            if s[i] != s[l-i-1]:
                temp1 = s[0:i]+s[i+1:]
                if temp1 == temp1[::-1]:
                    return True
                temp2 = s[:l-i-1] + s[l-i:]
                if temp2 == temp2[::-1]:
                    return True
                return False
        return False