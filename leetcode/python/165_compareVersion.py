class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        v1 = version1.split(".")
        v2 = version2.split(".")
        length = max(len(v1), len(v2))
        v1 = v1 + [0]*(length - len(v1))
        v2 = v2 + [0]*(length - len(v2))
        print v1, v2
        for i in range(length):
            num1 = int(v1[i])
            num2 = int(v2[i])
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
            else:
                continue
        return 0

sol = Solution()
print sol.compareVersion("1", "1.1")