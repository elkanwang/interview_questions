class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        direction = 1
        row = 0
        res = ["" for i in range(numRows)]
        for i in range(len(s)):
        	res[row] += s[i]
        	if numRows == 1:
        		continue
        	elif row == numRows -1:
        		direction = -1
        	elif row == 0:
        		direction = 1
        	
        	row = row + direction
        s = ''
        for i in range(len(res)):
        	s += res[i]
        return s

sol = Solution()
print sol.convert("asdff",2)