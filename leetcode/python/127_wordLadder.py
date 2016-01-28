from string import ascii_lowercase as lowercase
class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
        if beginWord == endWord:
            return 2
        wordDict.add(endWord)
        nextLvl = set()
        curLvl = set()
        visited = set()
        curLvl.add(beginWord)
        res = 1
        while endWord not in curLvl and len(curLvl)>0:
            nextLvl.clear()
            for word in curLvl:
                for nextWord in self.findNext(word, wordDict):
                    if nextWord not in visited:
                        nextLvl.add(nextWord)
                        visited.add(nextWord)
            res += 1
            curLvl = nextLvl.copy()
        if len(curLvl) ==0 and endWord not in curLvl:
            return 0
        return res

    def findNext(self, word, wordDict):
        res = set()
        for i in xrange(len(word)):
            for c in lowercase:
                newWord = word[:i]+c+word[i+1:]
                if newWord == word:
                    continue
                if newWord in wordDict:
                    res.add(newWord)
        return res

print Solution().ladderLength("hot", "dog", {"hot", "dog", "dot"})