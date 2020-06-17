class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        store = {0:1}
        cumulative_sum = 0
        res = 0
        for num in nums:
            cumulative_sum += num
            temp = cumulative_sum - k
            if temp in store:
                res += store[temp]
            store[cumulative_sum] = 1 + (store[cumulative_sum] if cumulative_sum in store else 0)
        return res

# The difference between two locations is what the sum of middle numbers is
