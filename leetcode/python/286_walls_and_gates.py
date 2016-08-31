class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        row = len(rooms)
        col = len(rooms[0])

        def explore(rooms, i, j, row, col):
            depth = 0
            cur_level = []
            cur_level.append((i, j))
            while cur_level:
                depth += 1
                next_level = []
                for cell_x, cell_y in cur_level:
                    for (x, y) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        new_cell_x, new_cell_y = cell_x + x, cell_y + y
                        if 0 <= new_cell_x < row and 0 <= new_cell_y < col:
                            if rooms[new_cell_x][new_cell_y] == -1 or rooms[new_cell_x][new_cell_y] == 0:
                                continue
                            else:
                                if depth < rooms[new_cell_x][new_cell_y]:
                                    rooms[new_cell_x][new_cell_y] = depth
                                    next_level.append((new_cell_x, new_cell_y))
                                else:
                                    continue
                cur_level = next_level

        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    explore(rooms, i, j, row, col)
                    # for row in rooms:
                    # print row


sol = Solution()
sol.wallsAndGates([])
sol.wallsAndGates(
    [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1],
     [0, -1, 2147483647, 2147483647]])
