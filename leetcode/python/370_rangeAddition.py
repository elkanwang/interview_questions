class Solution(object):
    def getModifiedArray(self, length, updates):
        arr = [0] * length
        for start, end, update_value in updates:
            for index in range(start, end+1):
                arr[index] += update_value
        return arr

sol = Solution()
print sol.getModifiedArray(5, [[1,3,2], [2,4,3], [0,2,-2]])