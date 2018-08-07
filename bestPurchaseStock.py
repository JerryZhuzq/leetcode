# 买卖股票的最佳时机②
class Solution(object):
    def maxProfit(self, prices):
        lens = len(prices)
        if lens <= 1:
            return 0
        mid = int(lens/2)
        left_price = prices[:mid]
        right_price = prices[mid:]
        max_left_price = self.maxProfit(left_price)
        max_right_price = self.maxProfit(right_price)
        left_right_price = max(right_price) - min(left_price)
        return max(max_right_price,max_left_price,left_right_price)

    def maxProfit2(selfs,prices):
        i = 0
        profit = 0
        for j in range(0,len(prices)):
            if prices[j] <= prices[i]:
                i = j
            if prices[j] > prices[i]:
                profit = profit + prices[j] - prices[i]
                i = j
                #i = j 将之后的差值也算进股票的最大利润 而不是i=j+1
        return profit

    def maxProfit3(selfs,prices):
        profit = 0
        for j in range(1,len(prices)):
            if prices[j] > prices[j-1]:
                profit = profit + prices[j] - prices[j-1]
                #maxProfit2的简化版
        return profit

r = Solution()
price = [7,1,5,4,6,3,6]
print(r.maxProfit3(price))
