class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        res = 0
        while (X < Y):
            res += 1
            if Y % 2 == 0:
                Y = Y // 2
            else:
                Y += 1
        return res + X - Y


