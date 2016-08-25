from collections import OrderedDict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = OrderedDict()
        for char in s:
            if char not in dict:
                dict[char] = 0
            else:
                dict[char] += 1
        for key, value in dict.items():
            if value == 0:
                return s.index(key)
        return -1

sol = Solution()
print(sol.firstUniqChar(''))
print(sol.firstUniqChar("loveleetcode"))