# class Solution(object):
#     def threeSumSmaller(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         nums = sorted(nums)
#         res = 0
#         for i in range(len(nums)-2):
#             for j in range(i+1, len(nums)-1):
#                 third_target = target - nums[i] - nums[j]
#                 index = self.find_index(nums, j+1, len(nums)-1, third_target)
#                 print i, j, index
#                 if nums[index] < third_target:
#                     res += index - j
#                 else:
#                     res += index - j - 1
#         return res
#
#
#     def find_index(self, nums, left, right, target):
#         while left < right:
#             mid = left + (right - left)/2
#             # print nums[mid]
#             if nums[mid] < target:
#                 # print nums[mid]
#
#                 left = mid + 1
#             else:
#                 if mid == left or nums[mid-1] < target:
#                     return mid
#                 right = mid - 1
#         return left


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        res = 0
        for i in range(len(nums)-2):
            start = i+1
            end = len(nums) - 1
            while start < end:
                # print i, start, end
                # print nums[i] + nums[start] + nums[end]
                if nums[i] + nums[start] + nums[end] < target:
                    res += (end - start)
                    start += 1
                else:
                    end -= 1
        return res

sol = Solution()
# print sol.find_index([1,2,3,4,5,6,7], 0, 6, 7)
print sol.threeSumSmaller([-2, 0, 1, 3], 2)
print sol.threeSumSmaller([0,0,0,0], 0)
print sol.threeSumSmaller([3,1,0,-2], 4)