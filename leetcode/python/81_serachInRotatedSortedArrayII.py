'''
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return -1
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return True
            if nums[left] < nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] == nums[left]:
                left += 1
            elif nums[mid] == nums[right]:
                right -= 1
        return False

sol = Solution()
print sol.search([4,6,7,7,7,7,0,1,1,2,2],2)
print sol.search([3,1,1],3)
