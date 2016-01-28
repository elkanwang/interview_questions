# coding=UTF-8

'''
Given an array S of n integers, are there elements a, b, c in S such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''

class Solution(object):
    '''
    Binary Search

    '''
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def binarySearch(l,r,number):
            pass
        res = set()
        nums = sorted(nums)
        print nums
        n = len(nums)
        if n<3:
            return []
        for i in xrange(n-2):
            for j in xrange(i+1,n-1):
                target = 0-nums[i]-nums[j]
                partial = nums[j+1:]
                if target in partial:
                    index = partial.index(target)
                    res.add((nums[i],nums[j],nums[j+1+index]))
                else:
                    continue
        return map(lambda x:list(x),res)

S = [-1,0,1 ,2 ,-1 ,-4]
sol = Solution()
print sol.threeSum(S)
