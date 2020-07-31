def maxProfit(prices) -> int:
    n = len(prices)
    if n < 2:
        return 0
    profit = [0 for x in range(n)]
    max_profit = 0
    i = n - 2
    while (i > -1):
        for j in range(i + 1, n):
            if prices[i] < prices[j]:
                if j >= n - 2:
                    profit[i] = max(profit[i], prices[j] - prices[i])
                else:
                    profit[i] = max(profit[i], prices[j] - prices[i] + profit[j + 2])
        i -= 1
        profit[i] = max(profit[i], profit[i + 1])
    return profit[0]

# dp O(n^2)


def maxProfit1(prices) -> int:
    if len(prices) == 0:
        return 0
    prof = [-prices[0], 0, 0]
    for i in range(1, len(prices)):
        # prof[0] stands for hold status, prof[1] stands for coolDown status, prof[2] stands for canBuy status
        prof[0], prof[1], prof[2] = max(prof[0], prof[2]-prices[i]), prof[0] + prices[i], max(prof[1], prof[2])
        print(prof)
    return max(prof)
# dp O(n)  prof = [hold, sell, cooldown(reset)]
# we should consider the stock problem as an investment problem, if we buy a stock,
# then current hold status should be equal to hold-stock

# hold = max(hold, cooldown-prices[i])
# obtain the maximum fund compared with either buy current stock after cooldown or keep the previous stock

# sell = prices[i] - hold
# straight forward, obtain the fund after sell stock in account

# cooldown = max(sell,
