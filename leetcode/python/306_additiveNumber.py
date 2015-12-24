'''
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the
first two numbers, each subsequent number in the sequence must be the sum of the
 preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence:
1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100,
199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence
1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine
if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?
'''


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) <= 2:
            return False
        for i in range(len(num)):
            for j in range(len(num)):
                if (i + j) >= len(num):
                    break
                if ( i >0 and num[0] == "0") or (j>0 and num[i+1] == "0") or num[i+j+2:] == "":
                    continue
                if (self.checkAcc(int(num[0:i+1]), int(num[i+1:i+2+j]), num[i+j+2:])):
                    return True
        return False

    def checkAcc(self, start1, start2, remaining):
        if (remaining == ""):
            return True
        newNum = str(start1 + start2)
        if (remaining.find(newNum) != 0):
            return False
        else:
            return self.checkAcc(start2, int(newNum), remaining[len(newNum):])

sol = Solution()
# print sol.isAdditiveNumber("112358")
# print sol.isAdditiveNumber("0")
# print sol.isAdditiveNumber("10")
print sol.isAdditiveNumber("111")
# print sol.isAdditiveNumber("211738")
print sol.isAdditiveNumber("198019823962")
print sol.checkAcc(19, 80, "19823962")
