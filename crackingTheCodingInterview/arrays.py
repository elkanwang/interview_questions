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

# q5.

# q6

# q7

# q8

# q9

# q10.


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

if __name__ == '__main__':
    unittest.main()
