class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        res = float('-inf')
        for num in nums:
            if num > 0:
                if cur <= 0:
                    cur = num
                else:
                    cur += num
            else:
                res = max(res, cur)
                cur += num
        return max(res, cur)

sol = Solution()
print sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])