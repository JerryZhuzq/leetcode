class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        if n < 1:
            return 0
        maxv = max(nums)
        offset = n * max(maxv, 1)
        if S >= 2*offset or S <= -2*offset:
            return 0
        res = {}
        res[nums[0]] = res.get(nums[0],0)+1
        res[-nums[0]] = res.get(-nums[0],0)+1
        for i in nums[1:]:
            temp = {}
            for j in res:
                temp[j+i] = temp.get(j+i, 0) + res[j]
                temp[j-i] = temp.get(j-i, 0) + res[j]
            res = temp
            # print(dp)
        return res.get(S,0)


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        if not nums: return 0
        total = sum(nums)
        if total < S or (total + S) % 2: return 0
        target = (total - S) // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for n in nums:
            for s in range(target, n - 1, -1):
                dp[s] += dp[s - n]
        return dp[-1]