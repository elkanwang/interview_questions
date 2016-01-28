class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        result = [1]
        while rowIndex > 0:
            copy = result[:]
            b = [1]
            for i in range(len(copy)-1):
                b.append(copy[i]+copy[i+1])
            b.append(1)
            result.append(b)
            rowIndex -= 1
            result = b[:]
        return result
    
sol = Solution()
print sol.getRow(1)