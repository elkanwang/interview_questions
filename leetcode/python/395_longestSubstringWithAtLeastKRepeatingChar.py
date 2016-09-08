class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        # convert string s to set
        # then use s.count as the function to count the occurrence.
        min_char = min(set(s), key=s.count)
        if s.count(min_char) >= k:
            return len(s)
        else:
            return max(self.longestSubstring(t, k) for t in s.split(min_char))

sol = Solution()
print sol.longestSubstring("aaabb",3)
print sol.longestSubstring("ababbc", 2)
print sol.longestSubstring("ababacb", 3)