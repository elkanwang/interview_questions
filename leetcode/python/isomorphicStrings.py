class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        length = len(s)
        if length != len(t):
        	return False
        dict1 = {}
        dict2 = {}
        for i in range(length):
            if ( s[i] in dict1 ):
                if t[i] not in dict2:
                    return False
                dict1[s[i]].append(i)
                dict2[t[i]].append(i)
                if cmp(dict1[s[i]], dict2[t[i]]) != 0:
                    return False
            else:
                dict1[s[i]] = [i]
                if t[i] in dict2:
                    return False
                dict2[t[i]] = [i]
        return True


print 4 % 3
sol = Solution()
print cmp([1,2,3],[1,2,3])