class Solution(object):

    # need to build a trie

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = set()
        for word in words:
            if word not in res and self.findWord(board, word):
                res.add(word)
        return list(res)

    def findWord(self, board, word):
        """
        return true if the word is inside the board
        :param board:
        :param word:
        :return:
        """
        def helper(board, mark_board, x, y, word, word_index):
            if word_index == len(word):
                return True
            if mark_board[x][y] == 1:
                return False
            if board[x][y] == word[word_index]:
                mark_board[x][y] = 1
                if len(word) == 1:
                    return True
                if x - 1 >= 0:
                    res = helper(board, mark_board, x-1, y, word, word_index+1)
                    if res:
                        return True
                if x + 1 < len(mark_board):
                    res = helper(board, mark_board, x+1, y, word, word_index+1)
                    if res:
                        return True
                if y - 1 >= 0:
                    res = helper(board, mark_board, x, y-1, word, word_index+1)
                    if res:
                        return True
                if y + 1 < len(board[0]):
                    res = helper(board, mark_board, x, y+1, word, word_index+1)
                    if res:
                        return True
                mark_board[x][y] = 0
                return False

        if (not board) or (not board[0]):
            return False
        mark_board = [[0] * len(board[0]) for i in range(len(board))]
        # print mark_board
        for i in range(len(board)):
            for j in range(len(board[0])):
                # print i, j
                if board[i][j] == word[0]:
                    if helper(board, mark_board, i, j, word, 0):
                        return True
        return False

sol = Solution()
print sol.findWords([['a']], 'a')