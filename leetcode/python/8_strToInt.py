import re

class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
    	str = re.findall('^[\+|-]?[0-9]+', str.strip())
        if str:
        	num = int(str[0])
        	MAX_INT = 2147483647
        	MIN_INT = -2147483648
        	if num > MAX_INT:
        		return MAX_INT
        	elif num < MIN_INT:
        		return MIN_INT
        	else:
        		return num
        else:
        	return 0

sol = Solution()
print sol.myAtoi('')