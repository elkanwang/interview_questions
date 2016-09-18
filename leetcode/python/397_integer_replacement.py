class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        dict = {}
        dict[1] = 0

        def helper(n):
            if n == 1:
                return 0
            else:
                if n in dict:
                    return dict[n]
                else:
                    if n %2 == 1:
                        dict[n] = min(helper(n+1), helper(n-1)) + 1
                    else:
                        dict[n] = helper(n/2) + 1
                    return dict[n]

        return helper(n)

sol = Solution()
print sol.integerReplacement(8)
print sol.integerReplacement(7)