class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
    	NUMERALS = {"I":1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    	romanNumbers = [] # list of roman numbers
        if len(s)==0:
        	return 0

        temp = ""
        while len(s) > 1:
            curNum = s[0]
            nextNum = s[1]
            if NUMERALS[curNum] >= NUMERALS[nextNum]: # reach the end of a roman number
            	temp += curNum
            	romanNumbers.append(temp)
            	temp = ""
            else:
            	temp += curNum
            s = s[1:]
        temp = temp+s[0]
        romanNumbers.append(temp)
        print romanNumbers
        # add all numbers together
        res = 0
        for i in range(len(romanNumbers)):
        	number = romanNumbers[i]
        	if len(number)==1:
        		res += NUMERALS[number[0]]
        	else:
        		res = res + NUMERALS[number[1]] - NUMERALS[number[0]]
        return res
        

sol = Solution()
print sol.romanToInt('MCMXCVI')