import re
class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        s = self.formatS(s)
        while len(s) > 1:
            if s[0] == s[len(s)-1]:
                s = s[1:-1]
            else:
                return False
        return True
            
    def formatS(self, s):
        regex = re.compile('\W')
        s = regex.sub('', s)
        return s.lower()

sol = Solution()
print sol.isPalindrome("1a2")