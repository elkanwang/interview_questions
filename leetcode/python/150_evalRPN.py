import math
class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
		operators = {'+', '-', '*', '/'}
		nums = []
		for token in tokens:
			if token in operators:
				num2 = nums.pop()
				num1 = nums.pop()
        		if token == "+":
        			nums.append(num1 + num2)
        		elif token == "-":
        			nums.append(num1 - num2)
        		elif token == "*":
        			nums.append(num1 * num2)
        		elif token == "/":
        			nums.append(int(num1*1.0 / num2))
			else:
				nums.append(int(token))
		return nums[0]

sol = Solution()
print sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])