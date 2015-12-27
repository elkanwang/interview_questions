'''
According to the Wikipedia's article: "The Game of Life, also known simply as
Life, is a cellular automaton devised by the British mathematician John Horton
Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead
(0). Each cell interacts with its eight neighbors (horizontal, vertical,
diagonal) using the following four rules (taken from the above Wikipedia
article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up:
Could you solve it in-place? Remember that the board needs to be updated at the
same time: You cannot update some cells first and then use their updated values
to update other cells.
In this question, we represent the board using a 2D array. In principle, the
board is infinite, which would cause problems when the active area encroaches
the border of the array. How would you address these problems?
'''


'''
To solve it in place, we use 2 bits to store 2 states:

[2nd bit, 1st bit] = [next state, current state]

- 00  dead (next) <- dead (current)
- 01  dead (next) <- live (current)
- 10  live (next) <- dead (current)
- 11  live (next) <- live (current)
In the beginning, every 2nd bit is 0.
When next state becomes alive, change 2nd bit to 1.
No need to consider case for transition 01 when lives < 2 || lives > 3.
In the end, revert every cell back.
For each cell, calculate num of live neighbors, and add the next state
by setting 2nd bit.

Transition 11: when board == 1 and lives >= 2 && lives <= 3, make 2nd bit to 1.
Transition 10: when board == 0 and lives == 3, make 2nd bit to 1.
To get the current state, simply do

board[i][j] & 1
To get the next state, simply do

board[i][j] >> 1

'''


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def calculateLives(i, j, row, col, board):
            count = 0
            for m in range(max(0,i-1), min(row,i+2)):
                for n in range(max(0,j-1), min(col,j+2)):
                    count += board[m][n] & 1
            return count - (board[i][j] & 1)

        if (not board or len(board)==0):
            return board
        row = len(board)
        column = len(board[0])
        for i in range(row):
            for j in range(column):
                lives = calculateLives(i, j, row, column, board)
                if ((board[i][j] & 1) == 1 and (lives >=2 and lives <=3)):
                    board[i][j] = 3
                if (board[i][j] & 1 == 0 and lives == 3):
                    board[i][j] = 2
        print board
        for i in range(row):
            for j in range(column):
                board[i][j] >>= 1

sol = Solution()
board =[[1,1],[1,0]]
sol.gameOfLife(board)
print board
