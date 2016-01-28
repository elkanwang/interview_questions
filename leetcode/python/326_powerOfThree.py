import math
class Solution(object):
    '''
    1. logrithm
    2. recursion
    3. loop
    '''
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n<0 else n == round(3 ** round(math.log(n, 3)))

sol = Solution()

print sol.isPowerOfThree(26)
