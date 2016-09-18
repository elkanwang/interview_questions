import collections
import random


class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice([i for i, num in enumerate(self.nums) if num == target])

sol = Solution([1,2,3,3,3])
print sol.pick(1)
print sol.pick(3)
