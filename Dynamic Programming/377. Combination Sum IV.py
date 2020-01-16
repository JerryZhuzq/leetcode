class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 1:
            return 0
        nums_set = set(nums)
        memo = [-1] * (target + 1)
        for i in nums:
            if target >= i:
                memo[i] = 1

        def subSum(target):
            for i in nums:
                if target > i:
                    if memo[target - i] != -1:
                        if target - i in nums_set:
                            memo[target] = max(0, memo[target])
                            memo[target] = max(0, memo[target] + subSum(target - i))
                            nums_set.remove(target - i)
                        else:
                            memo[target] = max(0, memo[target])
                            memo[target] += memo[target - i]
                    else:
                        memo[target] = max(0, memo[target])
                        memo[target] = max(0, memo[target] + subSum(target - i))
            return max(0, memo[target])

        return subSum(target)

    #   The diffculty lies in u should calculate every number even it is in the given list.
