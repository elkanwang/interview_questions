class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        res = 0
        for char in s:
            res ^= ord(char)
        for char in t:
            res ^= ord(char)
        return chr(res)

sol = Solution()
print sol.findTheDifference('abc', 'abcd')