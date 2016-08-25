# make a flag
# 1 means the current one is the largest
# -1 means the current one is the smallest
# going through the list,
# 1 => abandon the last number if this one is bigger
# -1 => abandon the last number if this one is smaller

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = None
        if len(nums)<=1:
            return len(nums)
        arr = nums[:1]
        index = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[0]:
                continue
            elif nums[i] < nums[0]:
                flag = -1
                index = i
                arr.append(nums[i])
                break
            else:
                flag = 1
                index = i
                arr.append(nums[i])
                break
        if flag == 0:
            return len(arr)
        for i in range(index+1, len(nums)):
            if nums[i] == arr[-1]:
                continue
            if nums[i] < arr[-1] and flag == -1:
                del arr[-1]
                arr.append(nums[i])
                continue
            elif nums[i] < arr[-1] and flag == 1:
                arr.append(nums[i])
                flag = -1
            if nums[i] > arr[-1] and flag == 1:
                del arr[-1]
                arr.append(nums[i])
                continue
            elif nums[i] > arr[-1] and flag == -1:
                arr.append(nums[i])
                flag = 1
        return len(arr)

s = Solution()
print(s.wiggleMaxLength([0]))
print(s.wiggleMaxLength([0,0]))
print(s.wiggleMaxLength([1,7,4,9,2,5]))
print(s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
