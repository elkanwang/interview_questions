'''
Given a positive integer n, find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13,
return 2 because 13 = 4 + 9.
'''
import math

class Solution(object):
    def getPerfectSquares(self, n):
        res = []
        for i in range(1, int(math.sqrt(n))+1):
            num = i * i
            if num <=n:
                res.append(num)
        return res


    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dpArr = [1000]*(n+1)
        dpArr[0] = 0
        for i in range(1, n+1):
            sqrt = int(math.sqrt(n))
            if i == sqrt * sqrt:
                dpArr[i] = 1
                continue
            else:
                for j in range(1, sqrt+1):
                    dpArr[i] = min(dpArr[i], 1 + dpArr[i-j*j])
        return dpArr[n]


# static dp array
# TODO: need to understand this

class Solution(object):
    numSquaresDP = [0]
    def numSquares(self, n):
        if len(self.numSquaresDP) <= n:
            perfectSqr = [v**2 for v in xrange(1, int(math.sqrt(n)) + 1)]
            for i in xrange(len(self.numSquaresDP), n + 1):
                self.numSquaresDP.append( min(1 + self.numSquaresDP[i - sqr] for sqr in perfectSqr if sqr <= i))
        return self.numSquaresDP[n]


sol = Solution()
print sol.getPerfectSquares(9)
print sol.numSquares(6175)
print sol.numSquares(12)
