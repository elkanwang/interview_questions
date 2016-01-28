class Solution(object):
    '''
    dp
    '''
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins = sorted(coins)
        index = len(coins) - 1
        counter = 0
        while index >=0 and amount >0:
            counter += amount / coins[index]
            amount %= coins[index]
            index-=1
        if amount >0:
            return -1
        else:
            return counter

sol = Solution()
print sol.coinChange([1,2,5], 11)
print sol.coinChange([186,419,83,408],6249)
