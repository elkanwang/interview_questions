class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if (not k) or (not s):
            return 0
        sofar_max = 0
        start = 0
        dict = {}
        for index, char in enumerate(s):
            if char in dict:
                dict[char] = index
                sofar_max = max(sofar_max, index - start + 1)
            else:
                if len(dict) < k:
                    dict[char] = index
                    sofar_max = max(sofar_max, index-start+1)
                else:
                    min_char = min(dict, key=dict.get)
                    min_index = dict[min_char]
                    # print min_char, min_index, char
                    del dict[min_char]
                    dict[char] = index
                    sofar_max = max(sofar_max, index-start)
                    start = min_index + 1
        return sofar_max

sol = Solution()
print sol.lengthOfLongestSubstringKDistinct('aa', 1)
print sol.lengthOfLongestSubstringKDistinct("eceba", 2)