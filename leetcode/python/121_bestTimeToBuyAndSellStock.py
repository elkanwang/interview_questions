class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        length = len(prices)
        if length==0:
            return 0
        temp = prices[length-1]
        res = 0
        for i in range(length-1,-1,-1):
            temp = max(temp,prices[i])
            if temp - prices[i] > res:
                res = temp - prices[i]
        return res