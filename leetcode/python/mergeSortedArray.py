class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        i=0
        j=0
        while i<m+j and j<n:
            if nums2[j] < nums1[i]:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j+=1
                i+=1
            else:
                i+=1
        while j < n:
            nums1[i] = nums2[j]
            i+=1
            j+=1

sol = Solution()
sol.merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5)
