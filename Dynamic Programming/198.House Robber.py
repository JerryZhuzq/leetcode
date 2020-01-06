class Solution:
    def rob(self, nums: List[int]) -> int:
        store = {}

        def memorySearch(index):
            res = 0

            if index > len(nums) - 1:
                return 0

            if index in store:
                return store[index]

            for i in range(index, len(nums)):
                res = max(res, nums[i] + memorySearch(i + 2))

            store[index] = res
            return res

        return memorySearch(0)

    # Top-Down

    class Solution:
        def rob(self, nums: List[int]) -> int:
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums[0], nums[1])
            store = {}
            n = len(nums)
            store[n - 1] = nums[n - 1]
            store[n - 2] = max(nums[n - 1], nums[n - 2])
            for i in reversed(range(n - 2)):
                res = max(store[i + 1], nums[i] + store[i + 2])
                store[i] = res
            return store[0]

    class Solution:
        def rob(self, nums: List[int]) -> int:
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums[0], nums[1])
            n = len(nums)
            store = [0 for i in range(n)]
            store[0] = nums[0]
            store[1] = max(store[0], nums[1])
            for i in range(2, n):
                store[i] = max(store[i - 1], nums[i] + store[i - 2])
            return max(store[n - 1], store[n - 2])


    # Bottom-Up