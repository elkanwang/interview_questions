class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
    	num.sort()
    	return num[len(num)/2]