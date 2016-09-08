import heapq

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if (not nums) or (not k):
            return []
        if len(nums) <= k:
            return [max(nums)]
        nums = map(lambda x: -x, nums)
        arr = []
        res = []
        for index in range(k):
            heapq.heappush(arr, nums[index])
        # print arr, res
        for index in range(k, len(nums)):
            res.append(- arr[0])
            arr.remove(nums[index-k])
            heapq.heapify(arr)
            heapq.heappush(arr, nums[index])
        res.append(-arr[0])
        return res
sol = Solution()
print sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
print sol.maxSlidingWindow([1], 1)
print sol.maxSlidingWindow([1, -1], 1)