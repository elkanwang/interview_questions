class Solution:
    # @return a list of integers
    def grayCode(self, n):
        result = [0]
        for i in range(n):
            result += [x + pow(2,i) for x in reversed(result)]
        return result