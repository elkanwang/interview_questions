class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        patternLen = len(pattern)
        strs = str.split()
        if patternLen != len(strs):
            return False
        pool = {}
        for i in range(patternLen):
            if pattern[i] in pool.keys():
                if pool[pattern[i]] != strs[i]:
                    return False
            else:
                if strs[i] in pool.values():
                    return False
                pool[pattern[i]] = strs[i]
        return True


sol = Solution()
sol.wordPattern("abc", "ab ab ab")
