import re

from collections import Counter
"""
    3. Longest Common Prefix 
"""
#class Solution:
#    # @param {string[]} strs
#    # @return {string}
#    def longestCommonPrefix(self, arr):
#        n = len(arr)
#        if n < 2:
#            return '' if not n else arr[0]

#        min_len = len(arr[0])
#        for i in range(1, n):
#            min_len = min(min_len, len(arr[i]))

#            for j in range(0, min_len):
#                if arr[i][j] != arr[i - 1][j]:
#                    min_len = j
#                    break

#            if min_len == 0:
#                return ''
        
#        return arr[0][:min_len]

#"""
#    Word Ladder
#"""
#class Solution:
#    # @param beginWord, a string
#    # @param endWord, a string
#    # @param wordDict, a set<string>
#    # @return an integer
#    def ladderLength(self, beginWord, endWord, wordDict):
#        from collections import defaultdict
#        if beginWord == endWord:
#            return 2

#        if not beginWord in wordDict:
#            wordDict.append(beginWord)
#        if not endWord in wordDict:
#            wordDict.append(endWord)

#        allwords = set()
#        for val in wordDict:
#            allwords.add(val)

#        res = 1
#        curr_level = set()
#        next_level = set()
#        curr_level.add(beginWord)
#        visited = set()
#        while curr_level:
#            if endWord in curr_level:
#                return res

#            for w in curr_level:
#                if w in visited:
#                    continue
#                visited.add(w)
#                next_level.update(self.find_neighbour(w, allwords))

#            curr_level = next_level
#            next_level = set()
#            res += 1
#        return 0

#    def find_neighbour(self, curr, wordDict):
#        res = set()
#        a = curr
#        for i in range(0, len(a)):
#            for j in 'abcdefghijklmnopqrstuvwxyz':
#                s = curr[:i] + j + curr[i + 1:]
#                if s != a and s in wordDict:
#                    seen.add(s)
#                    res.add(s)
#        return res


#class Solution:
#    # @param start, a string
#    # @param end, a string
#    # @param dict, a set of string
#    # @return a list of lists of string
#    def findLadders(self, start, end, wordDict):
#        from collections import defaultdict, deque

#        res = []
#        if start == end:
#            res.append([start])
#            return res

#        if not start in wordDict:
#            wordDict.append(start)
#        if not end in wordDict:
#            wordDict.append(end)

#        allwords = set()
#        for val in wordDict:
#            allwords.add(val)

#        wordDict = allwords
#        mp = defaultdict(set)
#        for w in wordDict:
#            for i in range(0, len(w)):
#                for j in 'abcdefghijklmnopqrstuvwxyz':
#                    s = w[:i] + j + w[i + 1:]
#                    if s in wordDict:
#                        mp[w].add(s)
        
#        curr_level = set()
#        next_level = set()
#        curr_level.add(start)
#        visited = defaultdict(set)
#        seen = set()
#        while curr_level:
#            if end in curr_level:
#                self.find_path(start, end, visited, [end], res)
#                return res

#            for w in curr_level:
#                seen.add(w)

#            for w in curr_level:
#                for ww in mp[w]:
#                    if ww == w or ww in seen:
#                        continue

#                    visited[ww].add(w)
#                    next_level.add(ww)

#            curr_level = next_level
#            next_level = set()

#        return res

#    def find_path(self, start, end, wordDict, path, res):
#        if start == end:
#            res.append(list(path[::-1]))
#        else:
#            for w in wordDict[end]:
#                if w in path:
#                    continue
#                path.append(w)
#                self.find_path(start, w, wordDict, path, res)
#                path.pop()



# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

#class Solution:
#    # @param {ListNode} l1
#    # @param {ListNode} l2
#    # @return {ListNode}
#    def addTwoNumbers(self, l1, l2):
#        if not l1 or not l2:
#            return l1 if l1 else l2

#        dummy = ListNode('*')
#        prev = dummy
#        carry = 0
#        while l1 and l2:
#            val = l1.val + l2.val + carry
#            prev.next = ListNode(val % 10)
#            prev = prev.next

#            carry = val / 10
#            l1, l2 = l1.next, l2.next

#        if l1 or l2:
#            rest = l1 if l1 else l2
#            prev.next = self.addTwoNumbers(rest, ListNode(carry))
#        elif carry:
#            prev.next = ListNode(1)
#        return dummy.next

#class Solution:
#    # @param {string} a
#    # @param {string} b
#    # @return {string}
#    def addBinary(self, a, b):
#        if not a or not b:
#            return a if not b else b

#        res = []
#        a = a[::-1]
#        b = b[::-1]
#        carry = 0

#        i = j = 0
#        while i < len(a) or j < len(b):
#            aval = int(a[i]) if i < len(a) else 0
#            bval = int(b[i]) if j < len(b) else 0
#            val = aval + bval + carry
#            res.append(val % 2)
#            carry = val / 2

#            i += 1
#            j += 1

#        if carry != 0:
#            res.append(1)

#        return ''.join(map(str, res)[::-1])

#class Solution:
#    # @param {string} a
#    # @param {string} b
#    # @return {string}
#    def addNumWithBase(self, a, b, base):
#        if not a or not b:
#            return a if not b else b

#        res = []
#        a = a[::-1]
#        b = b[::-1]
#        carry = 0

#        i = j = 0
#        while i < len(a) or j < len(b):
#            aval = int(a[i]) if i < len(a) else 0
#            bval = int(b[i]) if j < len(b) else 0
#            val = aval + bval + carry
#            res.append(val % base)
#            carry = val / base

#            i += 1
#            j += 1

#        if carry != 0:
#            res.append(1)

#        return ''.join(map(str, res)[::-1])


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return str(self.start) + '-' + str(self.end)

#class Solution:
#    # @param {Interval[]} intervals
#    # @return {Interval[]}
#    def merge(self, intervals):
#        if not intervals or len(intervals) == 1:
#            return intervals

#        intervals.sort(key=lambda x: x.start)

#        n = len(intervals)
#        res = []
#        curr = intervals[0]

#        for i in range(1, n):
#            if intervals[i].start > curr.end:
#                res.append(curr)
#                curr = intervals[i]
#            else:
#                curr.end = max(intervals[i].end, curr.end)
#        res.append(curr)
#        return res


#def most_n_frequest(s, n):
#    s = filter(lambda x: x != '', re.split('\n|\t|\s', s))
#    c = Counter(s)
#    return c.most_common(5)

#print most_n_frequest("""Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code. They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index.#collections.namedtuple(typename, field_names[, verbose=False][, rename=False])Returns a new tuple subclass named typename. The new subclass is used to create tuple-like objects that have fields accessible by attribute lookup as well as being indexable and iterable. Instances of the subclass also have a helpful docstring (with typename and field_names) and a helpful __repr__() method which lists the tuple contents in a name=value format.The field_names are a sequence of strings such as [x, y]. Alternatively, field_names can be a single string with each fieldname separated by whitespace and/or commas, for example x y or, y.Any valid Python identifier may be used for a fieldname except for names starting with an underscore. Valid identifiers consist of letters, digits, and underscores but do not start with a digit or undersco""", 3)


#class Solution:
#    # @param {string} s
#    # @return {boolean}
#    def isPalindrome(self, s):
#        if len(s) < 2:
#            return True

#        i = 0
#        j = len(s) - 1
#        while i < j:
#            if not s[i].isalnum():
#                i += 1
#            elif not s[j].isalnum():
#                j -= 1
#            else:
#                if s[i].lower() != s[j].lower():
#                    return False
#                i += 1
#                j -= 1

#        return True


#class Solution:
    # @param {string[]} strs
    # @return {string[]}
    #def anagrams(self, arr):
    #    from collections import defaultdict
    #    n = len(arr)
    #    if n < 2:
    #        return []
        
    #    m = defaultdict(list)
    #    for s in arr:
    #        ss = ''.join(sorted(list(s)))
    #        m[ss].append(s)

    #    res = []
    #    for key in m:
    #        if len(m[key]) > 1:
    #            res.extend(m[key])
    #    return res

#class Solution:
#    # @param {integer} numRows
#    # @return {integer[][]}
#    def generate(self, n):
#        res = []
#        if n == 0:
#            return res

#        res = [[1]]
#        for i in range(1, n):
#            curr = list(res[-1]) + [1]
#            for i in reversed(range(1, len(curr) - 1)):
#                curr[i] += curr[i - 1]
#            res.append(curr)
#        return res

#for line in Solution().generate(5):
#    print line

#class Solution:
#    # @param {integer} rowIndex
#    # @return {integer[]}
#    def getRow(self, rowIndex):
#        if rowIndex == 0:
#            return [1]

#        curr = [1]
#        for i in range(rowIndex):
#            curr.append(1)
#            for i in reversed(range(1, len(curr) - 1)):
#                curr[i] += curr[i - 1]
#        return curr

#print Solution().getRow(3)


#class Generator:
#    def __init__(self, probList):
#        l = [[c[0], c[1]] for c in probList]
#        for i in range(1, len(l)):
#            l[i][1] += l[i - 1][1]
#        self.probList = l

#    def genRandom(self):
#        import random
#        i = random.random()
#        j = 0
#        while j < len(self.probList) and i > self.probList[j][1]:
#            j += 1
#        j = min(j, len(self.probList) - 1)
#        return self.probList[j][0]

#g = Generator([('a', 0.25), ('b', 0.25), ('c', 0.5)])
#seen = {'a': 0, 'b': 0, 'c': 0}
#for i in range(30000):
#    seen[g.genRandom()] += 1
#print seen

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#class Solution:
#    # @param two ListNodes
#    # @return the intersected ListNode
#    def getIntersectionNode(self, f, g):
#        if not f or not g:
#            return None

#        ff = f
#        gg = g
#        len_f = len_g = 0
#        while ff:
#            len_f += 1
#            ff = ff.next
#        while gg:
#            len_g += 1
#            gg = gg.next

#        diff = abs(len_f - len_g)
#        longer = f if len_f > len_g else g
#        shorter = f if len_f <= len_g else g

#        while diff:
#            longer = longer.next
#            diff -= 1

#        while longer and shorter and not longer is shorter:
#            longer, shorter = longer.next, shorter.next

#        return longer

#count_inside = 0
#for count in range(0, 10000):
#    import math
#    import random
#    d = math.hypot(random.random(), random.random())
#    if d < 1: count_inside += 1
#    count += 1
#print 4.0 * count_inside / count


# compute sqrt of n to kth decimal precision
#def compute_sqrt(n, k):
#    if n == 1:
#        return 1

#    fs = "{:." + str(k) + "f}"
#    x = n / 2.
#    prev = fs.format(x)
#    x = (x + n / x) / 2
#    while fs.format(x) != prev:
#        prev = fs.format(x)
#        x = (x + n / x) / 2

#    return fs.format(x)

#n = 23012831
#print compute_sqrt(n, 6)
#print n ** 0.5



## longest common prefix

## word ladder II

## add two number
def addNumber(num1, num2, n):
	maxLen = max(len(num1), len(num2))
	num1 = " "*(maxLen - len(num1)) + num1
	num2 = " "*(maxLen - len(num2)) + num2
	residue = 0
	res = ""
	for i in range(maxLen-1, -1, -1):
		residue += int(num1[i]) + int(num2[i])
		res = str(residue % n) + res
		residue = residue / n
	if residue != 0:
		res = str(residue) + res
	return res

print addNumber("111", "222", 3)


# most occurring keyword
def mostOccuring(keywords):
	from collections import Counter
	ss = filter(lambda x: x!='', re.split("\s|\n|\t", keywords))
	print Counter(ss).most_common()

#method 2: heap
	
mostOccuring("asdf asdf 	 asdf")



def palindrome(s):
	s = s.strip()
	while len(s)>1:
		if s[0] = s[-1]:
			s = [1:-1]
		else:
			return False
	return True

def anagrams(words):



## http status
## 200 OK
## 400 bad request
## 401 unauthorized
## 403 forbidden
## 404 not found
## 300 multiple choice
## 301 permanent redirect
## 302 temporary redirect
## 304 not modified
## 500 internal server error
## 501 not implemented
## 502 bad gateway
## 503 service unavailable

## TCP v.s. UDP
## TCP
## Transmission Control Protocol
## connection-oriented
## suits application requires higher reliability, less time critical
## handshake: syn, syn-ack, ack
## http://www.cisco.com/web/about/ac123/ac147/archived_issues/ipj_9-4/syn_flooding_attacks.html

## UDP
## User Datagram Protocol
## connectionless

## web cache
## images, resources

## rendering a page
## https://friendlybit.com/css/rendering-a-web-page-step-by-step/