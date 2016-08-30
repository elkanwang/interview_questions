class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # this is the key, this makes operations faster
        # without making this set, it gives TLE
        nums = set(nums)
        best = 0
        for n in nums:
            if (n - 1) not in nums:
                m = n + 1
                while m in nums:
                    m += 1
                best = max(best, m - n)
        return best

sol = Solution()
print sol.longestConsecutive([100, 4, 200, 1, 3, 2])