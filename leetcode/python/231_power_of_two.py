class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n > 1:
            remainder = n % 2
            n = n / 2
            if remainder != 0:
                return False
        return True

sol = Solution()
print sol.isPowerOfTwo(21)
print sol.isPowerOfTwo(16)