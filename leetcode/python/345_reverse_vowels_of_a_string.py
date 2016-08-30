# class Solution(object):
#     def reverseVowels(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         indices = []
#         vowels = []
#         for index, char in enumerate(s):
#             if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
#                 indices.append(index)
#                 vowels.append(char)
#         vowel_count = len(vowels)
#         if not vowel_count:
#             return s
#
#         res = ""
#         vowel_index = 0
#         vowels = vowels[::-1]
#         for index, char in enumerate(s):
#             if index in indices:
#                 res += vowels[vowel_index]
#                 vowel_index+=1
#             else:
#                 res += char
#         return res

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str

        two pointer
        """
        if not s:
            return ""
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        start = 0
        end = len(s) - 1
        s = list(s)
        while start < end:
            while start < end and s[start] not in vowels:
                start += 1
            while start < end and s[end] not in vowels:
                end -= 1
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return ''.join(s)

sol = Solution()
print sol.reverseVowels('hello')