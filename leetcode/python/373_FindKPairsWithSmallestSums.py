import heapq

# class Solution(object):
#     def kSmallestPairs(self, nums1, nums2, k):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         if not (nums1, nums2, k):
#             return []
#         res = []
#         index_1 = 1
#         index_2 = 1
#         res.append([nums1[0], nums2[0]])
#         if k == 1:
#             return res
#         while index_1 < len(nums1) and index_2 < len(nums2):
#             if nums1[index_1] <= nums2[index_2]:
#                 res.append([nums1[index_1], nums2[index_2-1]])
#                 index_1 += 1
#             else:
#                 res.append([nums1[index_1 - 1], nums2[index_2]])
#                 index_2 += 1
#             if len(res) == k:
#                 return res
#         print(index_1, index_2)
#         for i in range(index_1, len(nums1)):
#             res.append([nums1[i], nums2[index_2-1]])
#             if len(res) == k:
#                 return res
#         for i in range(index_2, len(nums2)):
#             print(index_2)
#             res.append([nums1[index_1-1], nums2[i]])
#             if len(res) == k:
#                 return res
#         return res


# class Solution(object):
#     def kSmallestPairs(self, nums1, nums2, k):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         if not (nums1 and nums2 and k):
#             return []
#         arr = [[] for n in range(0, nums1[-1]+nums2[-1])]
#         for i in nums1:
#             for j in nums2:
#                 arr[i+j-1].append([i,j])
#         res = []
#         for list in arr:
#             for item in list:
#                 if k == 0:
#                     return res
#                 else:
#                     res.append(item)
#                     k -= 1
#         return res

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        h = []
        for i in nums1:
            for j in nums2:
                heapq.heappush(h, (i+j, [i,j]))
        res = []
        # print(h)
        for i in range(min(len(h), k)):
            res.append(heapq.heappop(h)[1])
        return res

s = Solution()
print(s.kSmallestPairs([1,1,2], [1,2,3], 10))
print(s.kSmallestPairs([-1,-1,-2], [-1,-2,-3], 6))


print(s.kSmallestPairs([1,2,3,4,5,6], [3,5,7,9], 3))