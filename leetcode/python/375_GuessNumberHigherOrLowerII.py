class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        my_guess = (n - 1) / 2 + 1
        payment = 0
        while high - low > 1:
            low = my_guess + 1
            payment += my_guess
            my_guess = (high - low ) / 2 + low
        return payment

s = Solution()
print(s.getMoneyAmount(10))
