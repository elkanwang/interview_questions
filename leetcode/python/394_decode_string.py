class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        def helper(s, start):
            # print s, start
            index = start
            res = ""
            while index < len(s):
                if s[index] in '0123456789':
                    multiplier_str = ""
                    while True:
                        if s[index] not in '0123456789':
                            break
                        multiplier_str += s[index]
                        index += 1
                    multiplier = int(multiplier_str)
                    substr, index = helper(s, index + 1)
                    res += multiplier * substr
                elif s[index] == '[':
                    pass
                elif s[index] == ']':
                    return res, index
                else:
                    res += s[index]
                index += 1
            return res, index
        return helper(s, 0)[0]


sol = Solution()
print sol.decodeString('2[a]')
print sol.decodeString('3[a]2[bc]')
print sol.decodeString('3[a2[c]]')
print sol.decodeString('')
print sol.decodeString('2[abc]3[cd]ef')