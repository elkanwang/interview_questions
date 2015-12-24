'''
Given a string which contains only lowercase letters, remove duplicate letters
so that every letter appear once and only once. You must make sure your result
is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
'''

'''
use bitwise operations.
set 1 to the letters that appear once and print them at the end '''


def removeDuplicateLetters(s):
    """
    :type s: str
    :rtype: str
    """
    counterArr = [0] * 26
    for char in s:
        counterArr[ord(char)-ord('a')] += 1
    print counterArr
    resultString = ""
    for char in s:
        if (counterArr[ord(char)-ord('a')] == 1):
            resultString += char
        else:
            counterArr[ord(char)-ord('a')]  -= 1
    return resultString

s1 = "bcabc"
s2 = "cbacdcbc"
s3 = "cbacdcbc"

print removeDuplicateLetters(s1)
print removeDuplicateLetters(s2)
print removeDuplicateLetters(s3)

