class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        i = 31
        newNumber = 0
        while i > 0:
            k = n & 1
            newNumber = newNumber | k
            newNumber = newNumber << 1
            n = n >> 1
            # print i, n
            i -= 1
        k = n & 1
        newNumber = newNumber | k
        return newNumber

sol = Solution()
print sol.reverseBits(2147483648)