class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if abs(dividend) < abs(divisor):
            return 0
        helper = True
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            helper = False
        abs_dividend, abs_divisor = abs(dividend), abs(divisor)
        power_divisor = abs_divisor
        count = 0
        list_divisor = []
        while power_divisor <= abs_dividend :
            ans = 2 ** count
            count += 1
            list_divisor.append((power_divisor, ans))
            power_divisor += power_divisor
        if count > 0:
            count -= 1
        res, sub_dividend = 0, abs_dividend
        while count >= 0:
            if res > 2**31 - 1:
                if dividend * divisor < 0:
                    return -2**31
                else:
                    return 2**31 -1
            if sub_dividend >= list_divisor[count][0]:
                sub_dividend -= list_divisor[count][0]
                res += list_divisor[count][1]
            else:
                count -= 1
        if helper:
            return res
        else:
            return -res

# The trick here is to implement doubling for divisor each time. And record
# the number of multiplication for each doubling result (2**count).
