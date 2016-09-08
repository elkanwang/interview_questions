class Solution(object):
    def isSubsequence(self, s, t):
        """
        :param s: str
        :param t: str
        :rtype: bool
        """
        if not s:
            return True
        cur_char = s[0]
        index = t.find(cur_char)
        if index == -1:
            return False
        while (not self.isSubsequence(s[1:], t[index+1:])) and index != -1:
            index = t.find(cur_char, index + 1)
        if index == -1:
            return False
        else:
            return True

sol = Solution()
print sol.isSubsequence('abc', 'ahbgdc')
print sol.isSubsequence('axc', 'ahbgdc')