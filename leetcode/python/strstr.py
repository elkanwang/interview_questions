class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        m = len(haystack)
        n = len(needle)
        i = 0
        if m == n == 0:
            return 0
        while i < m-n+1:
            if haystack[i:i+n]==needle:
                return i
            i+=1
        return -1

sol = Solution()
print sol.strStr("mississippi", "mississippi")
print sol.strStr("a", "aaa")
print sol.strStr("ana", "n")
print sol.strStr("mississippi", "issipi")