class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def build_paranthesis(left, right):
            # print left, right
            if left < 0 or right < 0:
                return []
            temp_res = []
            if left < right and right > 0:
                tmp = build_paranthesis(left, right-1)
                if tmp == []:
                    tmp += [[')']]
                else:
                    for brackets in tmp:
                        brackets.append(')')
                temp_res += tmp
            if left > 0:
                tmp = build_paranthesis(left-1, right)
                if tmp == []:
                    tmp += [['(']]
                else:
                    for brackets in tmp:
                        brackets.append('(')
                temp_res += tmp

            return temp_res
        return map(lambda x: ''.join(x[::-1]), build_paranthesis(n, n))

sol = Solution()
print sol.generateParenthesis(3)