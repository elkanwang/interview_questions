class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        w = s.split(' ')
        w.reverse()
        for i in range(len(w)):
        	if len(w[i])!=0:
        		return w[i]

sol = Solution()
print sol.lengthOfLastWord('hello ')