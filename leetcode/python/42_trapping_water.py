class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        current_max = 0
        res = 0
        max_height = max(height)
        max_index = height.index(max_height)

        for val in height[:max_index+1]:
            if val > current_max:
                current_max = val
            else:
                res += current_max - val
        current_max = 0
        for val in reversed(height[max_index:]):
            if val > current_max:
                current_max = val
            else:
                res += current_max - val
        return res

sol = Solution()
print sol.trap([0,1,0,2,1,0,1,3,2,3, 1,2,1])
