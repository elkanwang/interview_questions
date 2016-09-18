class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 9
        number_of_digits = 1
        while True:
            if n - m * number_of_digits * len(str(number_of_digits)) <= 0:
                print n, m, number_of_digits
                if number_of_digits == 1:
                    return n
                length = len(str(number_of_digits))
                number = number_of_digits + (n-1) / length
                return int(str(number)[(n - 1) % length])
            n -= m * number_of_digits * len(str(number_of_digits))
            number_of_digits *= 10

sol = Solution()
# print sol.findNthDigit(3)
# print sol.findNthDigit(15)
# print sol.findNthDigit(9)
print sol.findNthDigit(333333)