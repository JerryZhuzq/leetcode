class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        # k*(2*x+k+1)
        res = 0
        for i in range(1, int(sqrt(2 * N + 0.5) - 0.25) + 1):
            if (N - i * (i + 1) // 2) % i == 0:
                res += 1

        return res