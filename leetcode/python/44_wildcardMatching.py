# coding=UTF-8
'''
仔细思考一下这题的核心所在，发现问题和Regular Expression Matching的核心类似，其实还是'*'到
底要match多少个s中的char。'*'可以match 0/1/多个，所以我们需要在遇到'*'时依然要对不同情形进
行试探，而在试探失败之后怎么reset到之前的状态就是问题的核心了。这题使用额外的空间会Memory
Limit Exceeded，自然会想到那我们只能用two pointer了，于是问题进一步变成了：如果试探失败，
怎么reset这两个pointer到应该去的位置，或者说哪里才是它们应该去的位置。如果我们从匹配0个s中的
char开始试探，那么“试探失败”其实意味着我们用'*'来匹配的s中的char匹配少了，需要用一个'*'来匹配
更多s中的char，所以对于s的指针，应该reset到的位置应该是上一个被'*'匹配的char后面的第一个char，
而对于p的指针，因为我们永远从匹配0个开始，所以依然是reset到'*'之后的第一个char，代码如下：

http://www.cnblogs.com/icecreamdeqinw/p/4324962.html
'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        asterik = -1
        lastMatch = -1
        i = 0
        j = 0
        while i < len(s):
            if j<len(p) and (p[j]=='?' or s[i] == p[j]):
                i+=1
                j+=1
            elif j<len(p) and p[j]=='*':
                asterik = j
                lastMatch = i
                j+=1
            elif asterik != -1:
                j = asterik+1
                lastMatch += 1
                i = lastMatch
            else:
                return False
        while j < len(p):
            if p[j] == '*':
                j+=1
            else:
                break
        return j == len(p)
sol = Solution()
print sol.isMatch("aa","a") #→ false
print sol.isMatch("aa","aa*aa") #→ true
print sol.isMatch("aaa","aa")# → false
print sol.isMatch("aa", "a*") #→ true
print sol.isMatch("aa", "?*") #→ true
print sol.isMatch("ab", "?*") #→ true
print sol.isMatch("aab", "*a*b") #→ true
print sol.isMatch("aab", "a?*") #→ true
print sol.isMatch('aa', '*')
