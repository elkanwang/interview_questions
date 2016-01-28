class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        res = strs[0]
        for i in range(len(strs)):
            if len(strs[i]) < len(res):
                res = strs[i]
        for i in range(len(strs)):
            while len(res)>0:
                if strs[i][:len(res)] == res:
                    break
                else:
                    res = res[:-1]
            if len(res) == 0:
                break
        return res

sol = Solution()
print sol.longestCommonPrefix(['abasdf','abasdf', 'abasdf'])