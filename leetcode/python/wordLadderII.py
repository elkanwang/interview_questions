from string import ascii_lowercase as lowercase
import collections
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        tracker = collections.defaultdict(set)
        currentLevel = set()
        nextLevel = set()
        lvlTracker = collections.defaultdict(set)
        dict.add(end)
        currentLevel.add(start)
        while currentLevel and end not in currentLevel:
        	nextLevel.clear()
        	lvlTracker.clear()
        	for word in currentLevel:
        		for nextWord in self.findNext(word, dict):
        			if nextWord not in tracker:
        				nextLevel.add(nextWord)
        				lvlTracker[nextWord].add(word)
        	tracker.update(lvlTracker)
        	currentLevel = nextLevel.copy()
        return [] if not currentLevel and end not in currentLevel else self.generatePath(start,end,tracker)

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

    def generatePath(self, start, end, tracker):
    	res = [[end]]
    	while res[0][0] != start:
    		newRes = []
    		for path in res:
    			for last in tracker[path[0]]:
    				newRes.append([last]+path)
    		res = newRes
    	return res

print Solution().findLadders("hot", "got", {"hot","dog","dot"})