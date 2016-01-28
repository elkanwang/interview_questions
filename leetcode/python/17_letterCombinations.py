class Solution:
    # @return a list of strings, [s1, s2]

    '''
    helper function:
    @param: the exisiting list of letter Combinations
    @param: the new possibilities
    '''
    def generateRes(self, res, letters):
    	temp = []
    	for letter in letters:
    		if res == []:
    			temp.append(letter)
    		for result in res:
    			temp.append(result+letter)
    	return temp

    def letterCombinations(self, digits):
    	res = [""]
        for d in digits:
        	if int(d) == 2:
        		res = self.generateRes(res,['a','b','c'])
        	elif int(d) == 3:
        		res = self.generateRes(res,['d','e','f'])
        	elif int(d) == 4:
        		res = self.generateRes(res,['g','h','i'])
        	elif int(d) == 5:
        		res = self.generateRes(res,['j','k','l'])
        	elif int(d) == 6:
        		res = self.generateRes(res,['m','n','o'])
        	elif int(d) == 7:
        		res = self.generateRes(res,['p','q','r','s'])
        	elif int(d) == 8:
        		res = self.generateRes(res,['t','u','v'])
        	elif int(d) == 9:
        		res = self.generateRes(res,['w','x','y','z'])
        return res

        '''
       	solution from LeetCode Discussion
        '''
	def letterCombinationsImproved(self, digits):
		hashed = {'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], '5': ['j', 'k', 'l'], '6': ['m','n','o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w','x','y','z']}
		combo = hashed[digits[0]][:] if digits else [""]

		for dig_index in range(1, len(digits)):
			for i in hashed[digits[dig_index]]:
				new_list = combo[:]
				new_list = [j+i for j in new_list if len(j+i) == dig_index+1]
				combo.extend(new_list)

        return [j for j in combo if len(j) == len(digits)]



A = ['d','e','f']
sol = Solution()
# print sol.generateRes(A,['d','e','f'])
print sol.letterCombinations("")