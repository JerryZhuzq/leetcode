class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        tmp1 = 1
        if int(s[:2]) < 27 and s[1] != "0":
            tmp2 = 2
        elif int(s[:2]) > 27 and s[1] == "0":
            return 0
        else:
            tmp2 = 1

        for i in range(2, len(s)):
            tmp = tmp2 * (s[i] != "0") + tmp1 * (int(s[i - 1:i + 1]) < 27 and int(s[i - 1]) != 0)
            tmp1, tmp2 = tmp2, tmp

        return tmp2