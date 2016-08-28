class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        odd_nums = ['0', '1', '8']
        even_nums = ['00', '11', '88', '69', '96']
        if not num:
            return True
        elif len(num) == 1:
            return num in odd_nums
        else:
            return num[0]+num[-1] in even_nums and self.isStrobogrammatic(num[1:-1])

sol = Solution()
print sol.isStrobogrammatic('111')
print sol.isStrobogrammatic('0')
print sol.isStrobogrammatic('69')
print sol.isStrobogrammatic('88')
print sol.isStrobogrammatic('818')
