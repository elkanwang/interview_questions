import math

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n < 3:
            return 0
        status = [0,0] + [1] * (n-1)
        for i in range(2, n):
            if status[i] == 1:
                k = 2
                while k * i < n:
                    status[k * i] = 0
                    k += 1
        print status
        return sum(status)

sol = Solution()
print sol.countPrimes(5)