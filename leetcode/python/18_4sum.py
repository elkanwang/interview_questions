'''
Given an array S of n integers, are there elements a, b, c, and d in S such
that a + b + c + d = target? Find all unique quadruplets in the array which
gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order.
(ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()
        nums = sorted(nums)
        n = len(nums)
        if n<4:
            return []
        for i in xrange(n-3)
            for j in xrange(a+1,n-2):
                t = target - nums[i] - nums[j]
                left = j+1
                right = n-1
                if nums[left] + nums[right] == t:
                    res.add((nums[i],nums[j],nums[left],nums[right]))
                for j in xrange(i+1,n-1):
                    target = 0-nums[i]-nums[j]-nums
                partial = nums[j+1:]
                if target in partial:
                    index = partial.index(target)
                    res.add((nums[i],nums[j],nums[j+1+index]))
                else:
                    continue
        return map(lambda x:list(x),res)
