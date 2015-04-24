class Solution:

    def isHappy(self, n):
        '''
        determine if an integer is happy

        @param {integer} n
        @return {boolean}
        '''
        table = []
        n = self.convert(n)
        while n != 1:
            if n in table:
                return False
            else:
                table.append(n)
                n = self.convert(n)
        return True

    def convert(self, n):
        '''
        convert a integer to the sum of the square of digits

        @param {integer} n
        @return {integer} sum of digits
        '''
        res = 0
        while n > 0:
            temp = n % 10
            res += temp * temp
            n = n // 10
        return res


sol = Solution()
print sol.isHappy(13)
