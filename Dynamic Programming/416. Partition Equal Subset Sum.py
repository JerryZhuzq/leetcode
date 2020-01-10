class Solution:

    # Top-Down
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sum = sum(nums)
        if sum % 2 != 0 or sum < 1:
            return False
        memo = [[-1 for x in range(sum // 2 + 1)] for x in range(n + 1)]

        def tryPartition(index, sum):
            if sum == 0:
                return True

            if index < 0 or sum < 0:
                return False

            if memo[index][sum] != -1:
                return memo[index][sum]
            memo[index][sum] = (tryPartition(index - 1, sum) or tryPartition(index - 1, sum - nums[index]))
            return memo[index][sum]

        return tryPartition(n - 1, sum // 2)

    # Bottom-Up

    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        n = len(nums)
        for i in nums:
            sum += i
        if sum % 2 != 0 or sum < 1:
            return False
        target = int(sum/2)
        memo = [0 for x in range(target+1)]
        for i in range(target+1):
            memo[i] = (i == nums[0])
        for i in range(1, n):
            j = target
            while(j>=nums[i]):
                # print(j, memo)
                memo[j] = (memo[j] or memo[j-nums[i]])
                j -= 1
        return memo[target]


