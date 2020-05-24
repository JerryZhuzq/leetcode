class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res_l, res_r, length = -1, -1, len(s)
        from collections import Counter
        sdic = dict()
        matched_chars = 0
        l, r = 0, 0
        if len(t) < 1 or len(t) > len(s):
            return ""
        if len(t) == 1:
            return t if t in s else ""
        tdic = Counter(t)
        while (r < len(s)):
            if s[r] not in tdic:
                r += 1
            else:
                sdic[s[r]] = sdic.get(s[r], 0) + 1
                if sdic[s[r]] <= tdic[s[r]]:
                    matched_chars += 1
                if matched_chars == len(t):
                    while (True):
                        if s[l] in sdic:
                            if matched_chars < len(t):
                                break
                            if sdic[s[l]] == tdic[s[l]]:
                                matched_chars -= 1
                                if r - l + 1 <= length:
                                    res_l, res_r = l, r
                                    length = r - l + 1
                            sdic[s[l]] -= 1
                        l += 1
                r += 1
        if res_l < 0 or res_r < 0:
            return ""
        return s[res_l: res_r + 1]



