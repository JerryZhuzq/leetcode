class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        coins = sorted(coins)
        if n < 1:
            return -1
        min_coin = min(coins)
        if amount == 0:
            return 0
        if min_coin > amount:
            return -1
        memo = [-1] * (amount - min_coin + 1)
        for i in range(n):
            if coins[i] == amount:
                return 1
            if coins[i] > amount:
                coins = coins[:i]
                break
            memo[coins[i]-min_coin] = 1
        # print(memo)
        for i in range(amount - min_coin + 1):
            value = i + min_coin
            for j in coins:
                if value - j >= min_coin and memo[value-j-min_coin] != -1:
                    if memo[i] != -1:
                        memo[i] = min(memo[i], memo[value-j-min_coin] + 1)
                    else:
                        memo[i] = memo[value - j-min_coin] + 1
        return memo[-1]