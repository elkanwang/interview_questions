class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def factorial(number):
            res = 9
            start = 9
            for i in range(1, number):
                res *= start
                start -= 1
            return res
        arr = [0] * (n+1)
        arr[0] = 1
        for i in range(1, n+1):
            tmp = factorial(i)
            arr[i] = tmp + arr[i-1]
        return arr[-1]

sol  = Solution()
for i in range(10):
    print(sol.countNumbersWithUniqueDigits(i))

