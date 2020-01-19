class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.cache = collections.defaultdict(int)
        d = len(strs)
        store = [[0, 0] for x in range(d)]
        for i in range(d):
            num0, num1 = 0, 0
            for j in strs[i]:
                if j == "0":
                    num0 += 1
                elif j == "1":
                    num1 += 1
            store[i][0], store[i][1] = num0, num1

        def subFindMaxForm(nums, m, n, k):
            if len(nums) - 1 < k or m + n <= 0:
                return 0
            if (m, n, k) in self.cache:
                return self.cache[(m, n, k)]
            selected = 0
            if m >= nums[k][0] and n >= nums[k][1]:
                selected = subFindMaxForm(nums, m - nums[k][0], n - nums[k][1], k + 1) + 1
            not_selected = subFindMaxForm(nums, m, n, k + 1)
            self.cache[(m, n, k)] = max(selected, not_selected)
            return self.cache[(m, n, k)]

        return subFindMaxForm(store, m, n, 0)

# Memorization Top - Down

    class Solution:
        def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in strs:
                zeros, ones = i.count('0'), i.count('1')
                for x in range(m, -1, -1):
                    for y in range(n, -1, -1):
                        if x >= zeros and y >= ones:
                            dp[x][y] = max(dp[x][y], dp[x - zeros][y - ones] + 1)
            return dp[-1][-1]

# DP Bottom-Up