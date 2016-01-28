class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        n = len(s)
        if n < 2:
            return s
        minStart = 0
        maxLen = 1
        i = 0
        while i < n:
            if n - i < maxLen / 2:
                break
            front = i
            back = i
            while back < n-1 and s[back+1] == s[back]:
                back+=1
            while back < n-1 and front > 0 and s[front-1]==s[back+1]:
                front -= 1
                back += 1
            newLen = back-front+1
            if newLen > maxLen:
                maxLen = newLen
                minStart = front
            i += 1
        return s[minStart:minStart+maxLen]

sol = Solution()
print sol.longestPalindrome('bb')