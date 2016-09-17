class Node(object):

    def __init__(self, x):
        self.val = x
        self.children = []
        self.visited = False
        self.in_tree = False

    def insert(self, node):
        if node not in self.children:
            self.children.append(node)


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return
        if len(words) == 1:
            # get rid of duplicates
            return ''.join(set(words))

        nodes = {}
        for index in range(1, len(words)):
            word1 = words[index-1]
            word2 = words[index]
            min_len = min(len(word1), len(word2))
            for i in range(min_len):
                if word1[i] != word2[i]:
                    prev = nodes.get(word1[i], Node(word1[i]))
                    next = nodes.get(word2[i], Node(word2[i]))
                    nodes[word1[i]] = prev
                    nodes[word2[i]] = next
                    prev.insert(next)
                    break
                else:
                    if word1[i] not in nodes:
                        nodes[word1[i]] = Node(word1[i])
            for i in range(len(word1)):
                if word1[i] not in nodes:
                    nodes[word1[i]] = Node(word1[i])
            for i in range(len(word2)):
                if word2[i] not in nodes:
                    nodes[word2[i]] = Node(word2[i])

        def topological_sort(node, res):
            if node.visited:
                return
            node.in_tree = True
            for child in node.children:
                if child.in_tree:
                    raise RuntimeError('not DAG')
                topological_sort(child, res)
            node.in_tree = False
            node.visited = True
            res.append(node.val)
        res = []

        for node in nodes.values():
            try:
                topological_sort(node, res)
            except RuntimeError:
                return ''

        return ''.join(res[::-1])

sol = Solution()
print sol.alienOrder([ "wrt", "wrf", "er", "ett", "rftt"])
print sol.alienOrder([ 'z'])
print sol.alienOrder(["ab","adc"])
print sol.alienOrder(["vlxpwiqbsg","cpwqwqcd"])