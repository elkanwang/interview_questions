class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        result = []
        print result
        if numRows == 0:
            return result
        result.append([1])
        numRows -= 1
        while numRows > 0:
            copy = result[len(result)-1][:]
            b = [1]
            for i in range(len(copy)-1):
                b.append(copy[i]+copy[i+1])
            b.append(1)
            result.append(b)
            numRows -= 1
        return result

sol = Solution()
print sol.generate(2)