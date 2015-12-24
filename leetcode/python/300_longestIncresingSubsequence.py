'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?


DP
more reading: http://www.algorithmist.com/index.php/Longest_Increasing_Subsequence
'''

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return len(nums)
        record = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if (nums[i] > nums[j]):
                    record[i] = max(record[i], record[j] + 1)
        return max(record)

sul = Solution()
nums =  [10, 9, 2, 5, 3, 7, 101, 18]
print sul.lengthOfLIS(nums)
