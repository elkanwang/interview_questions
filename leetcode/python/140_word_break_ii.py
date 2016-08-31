class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        def helper(s, wordDict, memo, index):
            if index >= len(s):
                return True, []
            if memo[index]:
                return memo[index]
            sofar = []
            for i in range(len(s) - index + 1):
                if s[index:index+i] in wordDict:
                    is_true, remaining = helper(s, wordDict, memo, index+i)
                    # print s[index:index+i], is_true, remaining
                    if is_true is False and remaining is None:
                        continue
                    elif remaining == []:
                        sofar += [[s[index:index+i]]]
                    else:
                        for word_list in remaining:
                            sofar += [[s[index:index+i]] + word_list]
            # print index, sofar
            if sofar:
                memo[index] = True, sofar
            else:
                memo[index] = False, None
            return memo[index]

        memo = [None] * len(s)
        _, res = helper(s, wordDict, memo, 0)
        return map(lambda x: ' '.join(x), res) if res else []

sol = Solution()
print sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
print sol.wordBreak("catsanddog", [])
print sol.wordBreak("catsandabddog", ["cat", "cats", "and", "sand", "dog"])