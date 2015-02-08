class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        charUsed = {}
        start = curMax = 0
        for n,char in enumerate(s):
            if char in charUsed and charUsed[char] >= start:
                start = charUsed[char]+1
                charUsed[char] = n
            else:
                charUsed[char] = n
                curMax = max(curMax, n-start+1)
        return curMax