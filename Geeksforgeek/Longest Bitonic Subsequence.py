def longestBitonicSubseq(nums):
    n = len(nums)
    if n < 1:
        return 0
    memo = [[0, 0] for x in range(n)]
    memo[0] = [1,1]
    res = 0
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j]:
                memo[i][0] = max(memo[i][0], memo[j][0] + 1)
                memo[i][1] = max(memo[i][0], memo[i][1])
                res = max(res, memo[i][1])
            elif nums[i] < nums[j]:
                memo[i][1] = max(memo[i][1], memo[j][1] + 1)
                res = max(res, memo[i][1])
    return res


print(longestBitonicSubseq([40, 30, 90, 80, 60, 30, 40, 20, 10]))