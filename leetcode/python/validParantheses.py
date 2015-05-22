class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        openBrackets = {"{", "[", "("}
        array = []
        for i in range(len(s)):
            if s[i] in openBrackets:
                array.append(s[i])
            else:
                if self.isPair(array, s[i]):
                    array.pop()
                else:
                    return False
        if len(array) == 0:
            return True
        else:
            return False
            
    def isPair(self, array, s):
        if len(array)==0:
            return False
        else:
            return (s==")" and array[-1]=="(") or (s=="]" and array[-1]=="[") or (s=="}" and array[-1]=="{")

sol = Solution()
print sol.isValid('{}()[][)')