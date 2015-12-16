import unittest
import re

# solutions for Chapter 1: Arrays


class Solution():
    ''' Solution'''

# q1. determine if an array has all unique characters

    def uniqueChar(self, string):
        pool = {}
        for char in string:
            if char in pool.keys():
                return False
            else:
                pool[char] = 1
        return True

# q2. implement void reverse(char* str)

#    def reverseString(string):
#        strLen = 0
#        while string[strLen] is not None:
#            strLen += 1
#        char *newStr[strLen]
#        for i in range(0,strLen):
#            newStr[i] = string[strLen-i]
#        return newStr

# q3. given two strings, determine if one is permutation of the other
# this is the same question as "anagram"

    def isPermutation(self, str1, str2):
        str1 = ''.join(sorted(str1))
        str2 = ''.join(sorted(str2))
        return str1 == str2

    def isPermutation2(self, str1, str2):
        pool = {}
        for char in str1:
            pool[char] = 1 if char not in pool.keys() else pool[char] + 1
        for char in str2:
            if char not in pool.keys():
                return False
            else:
                pool[char] -= 1
        for value in pool.values():
            if value != 0:
                return False
        return True

# q4. replace whitespace with %20, implement in-place solution

    def replaceSpace(self, s):
        s = re.sub(r' ', '%20', s)
        return s

    def replaceSpace2(self, s):
        pass

# q5. basic string compression, if the compressed string is longer than the
#       original string, return the original string
#       assume there's only upper case and small case letters
#       e.g. aabcccccaaa -> a2b1c5a3

# q6. M*N matrix, each entry is 4 bytes, rotate the matrix by 90 degree
    def swapMatrix(self, matrix, res, n, i, j):
        '''
        helper function to swap two entries in the matrix
        '''
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][n-i-1]
        matrix[j][n-i+1] = temp

    def rotateMtrix(self, matrix):
        '''
        the solution of the question is quite simple, the trick
        is to find the correct formula for rotating the matrix.
        That is:
        for i representing the row number
        and j representing the column number
        maxtrix[i][j] = matrix[j][n-i-1]
        we just need a helper function to swap this two entry
        '''
        dimension = len(matrix)
        res = matrix[:][:]
        for i in range(dimension):
            for j in range(dimension):
                res[j][dimension-i+1] = matrix[i][j]
        return res

# q7. if an element in M*N is 0, its entire row and column are set to 0

# q8. assume having a function called isSubString. Given two strings, check if
#       s2 is a rotation of s1.
#       e.g. 'waterbottle' is a rotation of 'erbottlewat'

    def isRotatedString(self, s1, s2):
        '''
        The straight forward solution to this problem is brute force.
        traverse the entire s1 and constantly making the new string
        check if they are the same string
        '''
        len1 = len(s1)
        len2 = len(s2)
        if len1 != len2:
            return False
        for index in range(len1):
            tempS = s1[index:] + s1[:index]
            if tempS == s2:
                return True
            else:
                continue
        return False

    def isRotatedStringImproved(self, s1, s2):
        len1 = len(s1)
        len2 = len(s2)
        if len1 != len2:
            return False
        s1 = s1 + s1
        return s2 in s1


class Test(unittest.TestCase):

    def testUniqueChar(self):
        self.assertEqual(Solution().uniqueChar('abc'), True)

    def testUniqueChar2(self):
        self.assertEqual(Solution().uniqueChar('aaa'), False)

    def test1(self):
        self.assertEqual(Solution().isPermutation('aaa', 'bbb'), False)

    def test2(self):
        self.assertEqual(Solution().isPermutation('abcdef', 'fecbad'), True)

    def test3(self):
        self.assertEqual(Solution().isPermutation2('aaa', 'bbb'), False)

    def test4(self):
        self.assertEqual(Solution().isPermutation2('abcdef', 'fecbad'), True)

    def test5(self):
        self.assertEqual(Solution().replaceSpace('a a'), 'a%20a')

    def test6(self):
        self.assertEqual(Solution().isRotatedStringImproved('watermelon', 'melonwater'), True)

    def test7(self):
        self.assertEqual(Solution().isRotatedStringImproved('watermelon', 'water'), False)

    def test8(self):
        self.assertEqual(Solution().isRotatedString('watermelon', 'melonwater'), True)

    def test9(self):
        self.assertEqual(Solution().isRotatedString('watermelon', 'water'), False)


if __name__ == '__main__':
    unittest.main()
