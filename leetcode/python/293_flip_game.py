class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for i in range(len(s)-1):
            if s[i] == '+' and s[i+1] == '+':
                res.append(s[:i]+'--'+s[i+2:])
        return res


sol = Solution()
print sol.generatePossibleNextMoves('++++')