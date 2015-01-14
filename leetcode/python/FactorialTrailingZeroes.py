class Solution:
    # @return an integer
    def trailingZeroes(self, n):
    	ret = 0
        while n>0:
        	ret += n/5
        	n = n/5
        return ret