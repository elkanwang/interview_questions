'''
Given an integer array nums, find the sum of the elements between indices i and
j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to
val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is
distributed evenly.
'''


class NumArray(object):
    sumArr = []
    nums = []
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        acc = 0
        for i in range(len(self.sumArr)):
            self.sumArr.pop()
        for i in range(len(self.nums)):
            self.nums.pop()
        self.nums = nums
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
        if i <1:
            return self.sumArr[j]
        return self.sumArr[j] - self.sumArr[i-1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        oldVal = self.nums[i]
        diff = val - oldVal
        self.nums[i] = val
        for i in range(i+1):
            self.sumArr[i] -= diff

# class NumArray(object):
    # def __init__(self, nums):
        # self.update = nums.__setitem__
        # self.sumRange = lambda i, j: sum(nums[i:j+1])
#python trick

# Your NumArray object will be instantiated and called as such:
nums = [1,3,5]
numArray = NumArray(nums)
print numArray.sumRange(0, 1)
numArray.update(1, 10)
print numArray.sumRange(1, 2)
