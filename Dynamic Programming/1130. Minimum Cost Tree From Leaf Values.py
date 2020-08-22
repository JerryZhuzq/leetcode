class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # from functools import lru_cache
        # @lru_cache(None)
        memo = [[0] * len(arr) for _ in range(len(arr))]
        def dp(left, right):
            if memo[left][right]:
                return memo[left][right]
            if left == right:
                return 0
            if left + 1 == right:
                return arr[left] * arr[right]
            # print(left, right)
            res = sys.maxsize
            for i in range(left, right):
                res = min(res, max(arr[left:i+1])*max(arr[i+1:right+1])+dp(left, i)+dp(i+1, right))
            memo[left][right] = res
            return res
            # return min(max(arr[left:i+1])*max(arr[i+1:right+1])+dp(left, i)+dp(i+1, right) for i in range(left, right))
        return dp(0, len(arr)-1)


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        for i in range(n):
            arr[i] = [arr[i], arr[i]]
        # print(arr)
        res = 0
        while len(arr) > 1:
            product = sys.maxsize
            idx = 0
            bigger = 0
            for i in range(1, len(arr)):
                # print(arr, i)
                if product > arr[i][0] * arr[i-1][0]:
                    product = arr[i][0] * arr[i-1][0]
                    bigger = max(arr[i][0], arr[i-1][0])
                    idx = i
            arr = arr[:idx-1] + [[bigger, product]] + arr[idx+1:]
            res += product
        return res
# a faster solution, the trick here is that in every iteration we need to find the two
# adjacent number with the minimum product and pop the small one and update the sum until
# only one value left in the array
