'''
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]

'''


class Solution(object):
#     def isValid(self, s):
        # count = 0
        # for char in s:
            # if char == '(':
                # count += 1
            # elif char == ')':
                # if count == 0:
                    # return False
                # else:
                    # count -= 1
        # if count == 0:
            # return True
        # else:
            # return False


    def dfs(self, s, index, cl, cr, openBracket, res, curS):
        # print s, index, cl, cr, openBracket, curS
        if (index == len(s) and cl == 0 and cr==0 and openBracket == 0):
            res.add(curS)
        if (index == len(s) or cl <0 or cr <0 or openBracket <0):
            return
        char = s[index]
        if char == '(':
            self.dfs(s, index+1, cl-1, cr, openBracket, res, curS)
            self.dfs(s, index+1, cl, cr, openBracket+1, res, curS+char)
        elif char == ')':
            self.dfs(s, index+1, cl, cr-1, openBracket, res, curS)
            self.dfs(s, index+1, cl, cr, openBracket-1, res, curS+char)
        else:
            self.dfs(s, index+1, cl, cr, openBracket, res, curS+char)

    def removeInvalidParentheses(self, s):
        countLeft = 0
        countRight = 0
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                if count == 0:
                    countRight += 1
                else:
                    count -= 1
        countLeft = count
        res = set()
        # print countLeft, countRight
        self.dfs(s, 0, countLeft, countRight, 0, res, "")
        return [i for i in res]

    # def removeInvalidParentheses(self, s):
        # """
        # :type s: str
        # :rtype: List[str]
        # """
        # countLeft = 0
        # countRight = 0
        # count = 0
        # for char in s:
            # if char == '(':
                # count += 1
            # elif char == ')':
                # if count == 0:
                    # countRight += 1
                # else:
                    # count -= 1
        # countLeft = count

        # lenRequired = len(s) - countLeft - countRight
        # result = []
        # visited = []
        # stack = []
        # stack.append(s)
        # while (stack):
            # s = stack.pop()
            # visited.append(s)
            # if (len(s) == lenRequired and self.isValid(s)):
                # if s in result:
                    # pass
                # else:
                    # result.append(s)
            # else:
                # for i in range(len(s)):
                    # if s[i] != '(' and s[i] != ')':
                        # pass
                    # else:
                        # temp = s[:i] + s[i+1:]
                        # if temp in visited:
                            # pass
                        # else:
                            # stack.append(temp)

        # return result

sol = Solution()
s1 =  "()())()"
s2 = "(a)())()"
s3 = ")(((((((("
s4 = "))y((())()())(((("
print sol.removeInvalidParentheses(s1)
print sol.removeInvalidParentheses(s2)
print sol.removeInvalidParentheses(s3)
print sol.removeInvalidParentheses(s4)
