'''
Given an array S of n integers, find three integers in S such that the sum is
closest to a given number, target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
import sys
import math
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n<=3:
            return sum(nums)
        nums = sorted(nums)
        mindiff = sys.maxint
        for i in range(n-2):
            left,right = i+1, n-1
            while (left < right):
                diff = nums[left] + nums[i] + nums[right] - target
                print i, left, right, diff
                if abs(diff) < abs(mindiff):
                    mindiff = diff
                if diff == 0:
                    return target
                    # break
                elif diff < 0:
                    left += 1
                else:
                    right -=1
        return target + mindiff

sol = Solution()
print sol.threeSumClosest([-1, 2, 1, -4],1)
