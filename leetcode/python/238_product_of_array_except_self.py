# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         if len(nums) < 2:
#             return []
#         left = [None] * len(nums)
#         right = [None] * len(nums)
#         cur = 1
#         for index, n in enumerate(nums):
#             cur *= nums[index]
#             left[index] = cur
#         cur = 1
#         for index, n in enumerate(reversed(nums)):
#             cur *= n
#             right[len(nums)-index-1] = cur
#         res = [None] * len(nums)
#         print left, right
#         for i in range(len(nums)):
#             if i == 0:
#                 res[i] = right[i+1]
#             elif i == len(nums)-1:
#                 res[i] = left[i-1]
#             else:
#                 res[i] = left[i-1]*right[i+1]
#         return res

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        res[0] = 1
        for index in range(1, len(nums)):
            res[index] = res[index-1] * nums[index-1]
        right = 1
        for index in reversed(range(len(nums))):
            res[index] *= right
            right *= nums[index]
        print res
        
sol = Solution()
sol.productExceptSelf([1,2,3,4])