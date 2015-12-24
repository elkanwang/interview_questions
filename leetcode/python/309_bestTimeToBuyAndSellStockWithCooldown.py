'''
Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (ie, buy one and sell one share of the stock
multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must
sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1
day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <=1:
            return 0
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])

        dpSells = [0] * len(prices)
        dpBuys = [0] * len(prices)
        dpCooldowns = [0] * len(prices)
        # dpNothings = [0] * len(prices)
        days = len(prices)

        dpBuys[0] = - prices[0]

        for i in range(2, len(prices)):
            # sells
            for j in range(i):
                dpSells[i] = max(dpSells[i], prices[j]-prices[i]+dpBuys[i])
            # buys
                dpBuys[i] = max(dpBuys[i], dpCooldowns[j])
            # cooldowns
                dpCooldowns[i] = max(dpCooldowns[i], dpSells[j])
            # dpnothings
        return max(dpSells[days-1], dpBuys[days-1], dpCooldowns[days-1])

prices = [1, 2, 3, 0, 2]
sol = Solution()
print sol.maxProfit(prices)
