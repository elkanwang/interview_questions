
# solutions for Chapter 1: Arrays


class Solution():
    ''' Solution'''

# q1. determine if an array has all unique characters

    def uniqueChar(string):
        strLen = len(string)
        if strLen == 0:
            return True
        pool = {}
        for char in string:
            if char in pool.keys():
                return False
            else:
                pool[char] = 1

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

    def isPermutation(str1, str2):
        str1.sort()
        str2.sort()
        return str1 == str2

# q4. replace whitespace with %20, implement in-place solution
