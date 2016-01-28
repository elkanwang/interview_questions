class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = s.split(' ')
        words.reverse()
        word = ""
        print words
        for i in range(len(words)):
        	if words[i] == "":
        		continue
        	word += " " + words[i]
        return word.strip()

sol = Solution()
print sol.reverseWords("   a   b ")