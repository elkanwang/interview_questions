class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = 0
        for char in set(s):
            if s.count(char) %2 == 1:
                count += 1
        if count <= 1:
            return True
        return False