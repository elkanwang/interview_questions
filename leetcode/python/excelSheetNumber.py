class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        res = 0
        while len(s) > 0:
            k = s[0]
            res *= 26
            res += (ord(k) - ord("A") + 1 )
            s = s[1:]
        return res