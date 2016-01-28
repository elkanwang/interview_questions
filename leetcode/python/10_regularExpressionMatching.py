# coding=UTF-8
'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''

class Solution(object):
    '''
    题意：’.’表示可以代替任何字符，’*’表示可以代替前面一个出现的字符，且可以代表任意个，
    给定字符串s和p，问s和p是否匹配。
    aab和c*a*b为true时因为，p中第一个*代替0个c，第二个*代替两个a，于是可以变为aab，
    和s相同，所以为true
    If the next character of p is NOT ‘*’, then it must match the current
    character of s. Continue pattern matching with the next character of both
    s and p.
    If the next character of p is ‘*’, then we do a brute force exhaustive
    matching of 0, 1, or more repeats of current character of p… Until we
    could not match any more characters.
    '''
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        if p[-1] == "*":
            if self.isMatch(s,p[:-2]):
                return True
            if s and (s[-1]==p[-2] or p[-2]=="."):
                return self.isMatch(s[:-1], p)
        else:
            if s and (s[-1]==p[-1] or p[-1]=="."):
                return self.isMatch(s[:-1], p[:-1])
            else:
                return False
        return False

sol = Solution()
print sol.isMatch("aa","a") #→ false
print sol.isMatch("aa","aa*aa") #→ true
print sol.isMatch("aaa","aa")# → false
print sol.isMatch("aa", "a*") #→ true
print sol.isMatch("aa", ".*") #→ true
print sol.isMatch("ab", ".*") #→ true
print sol.isMatch("aab", "c*a*b") #→ true
print sol.isMatch("aab", "b.*") #→ true
