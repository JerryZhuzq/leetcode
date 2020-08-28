class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_stock = sys.maxsize
        potential_val = 0
        res = 0
        for i in prices:
            if i < cur_stock:
                cur_stock = i
                res += potential_val
                potential_val = 0
            else:
                if i - cur_stock > potential_val:
                    potential_val = i-cur_stock
                else:
                    res += potential_val
                    cur_stock = i
                    potential_val = 0
        return res+potential_val


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = [0 for i in range(len(prices))]
        for i in range(len(prices) - 1):
            arr[i + 1] = prices[i + 1] - prices[i]

        maxProfit = 0
        for i in range(len(arr)):
            if arr[i] > 0:
                maxProfit += arr[i]
        return maxProfit
