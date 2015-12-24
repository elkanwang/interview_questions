'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''

class NumArray(object):
    sumArr = []
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        acc = 0
        for i in range(len(self.sumArr)):
            self.sumArr.pop()
        for i in nums:
            acc += i
            self.sumArr.append(acc)
        print self.sumArr


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        print self.sumArr[i], i
        if i <1:
            return self.sumArr[j]
        return self.sumArr[j] - self.sumArr[i-1]

# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(nums)
print numArray.sumRange(0, 1)
print numArray.sumRange(1, 2)

nums2 = [-1]
numA = NumArray(nums2)
print numArray.sumRange(0,0)
