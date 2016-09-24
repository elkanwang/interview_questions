class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):

        def reverse(start, end):
            mid = (end - start+1) / 2 + start
            for i in range(start, mid):
                # print i, s
                tmp = s[i]
                s[i] = s[end - i + start]
                s[end - i + start] = tmp

        n = len(s)
        reverse(0, n-1)
        start = 0
        for i in range(n):
            if s[i] == ' ':
                reverse(start, i-1)
                start = i+1
        # print start, n-1, s
        reverse(start, n-1)
        print s

sol = Solution()
sol.reverseWords( ['h','e','l','l','o',' ', 'w', 'o', 'r', 'l', 'd', '!'])