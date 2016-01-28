class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        pool = set()
        ans = set()
        for i in range(len(s)-9):
            curS = s[i:i+10]
            if curS in pool:
                ans.add(curS)
            else:
                pool.add(curS)
        return list(ans)

sol = Solution()
print sol.findRepeatedDnaSequences('AAAAAAAAAA')