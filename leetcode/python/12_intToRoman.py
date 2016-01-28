def helper(res, first, fifth, tenth, num):
    if num <= 3:
        return res + num*first
    elif num == 4:
        return res + first + fifth
    elif num == 5:
        return res + fifth
    elif num <= 8:
        return res + fifth + (num-5)*first
    elif num == 9:
        return res + first + tenth

class Solution:
    # @return a string
    def intToRoman(self, num):
    	# I V X
        # X L C
        # C D M
        res = ''
        res = helper(res,'M','L','L', num // 1000 )
        num = num % 1000
        res = helper(res,'C','D','M', num // 100 )
        num = num % 100
        res = helper(res,'X','L','C', num // 10 )
        num = num % 10
        res = helper(res,'I','V','X', num)
        return res
