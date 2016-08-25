# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        my_guess = (n - 1) /2
        while high >= low:
            res = guess(my_guess)
            if res == 0:
                return my_guess
            elif res == 1:
                low = my_guess + 1
            elif res == -1:
                high = my_guess - 1
            my_guess = (high - low ) / 2 + low
