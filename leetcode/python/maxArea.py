class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        area = 0
        while left < right:
            print left, right, height[left],height[right], min(height[left],height[right]), (right-left)
            area = max(min(height[left],height[right])*(right-left), area)
            if height[left]<height[right]: left+= 1
            else: right-=1
        return area

sol = Solution()
print sol.maxArea([1,1])