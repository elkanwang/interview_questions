class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        row = len(grid)
        col = len(grid[0])
        row_list = []
        col_list = []
        for row_i in range(row):
            start = 0
            index = 0
            count = 0
            cur_row = []
            while index < col:
                if grid[row_i][index] == 'E':
                    count += 1
                elif grid[row_i][index] == 'W':
                    if start != index:
                        if count != 0:
                            cur_row.append((start, index-1, count))
                    start = index + 1
                    count = 0
                index += 1
            if count != 0:
                cur_row.append((start, index-1, count))
            row_list.append(cur_row)

        for col_i in range(col):
            start = 0
            index = 0
            count = 0
            cur_col = []
            while index < row:
                if grid[index][col_i] == 'E':
                    count += 1
                elif grid[index][col_i] == 'W':
                    if start != index:
                        if count != 0:
                            cur_col.append((start, index - 1, count))
                    start = index + 1
                    count = 0
                index += 1
            if count != 0:
                cur_col.append((start, index-1, count))
            col_list.append(cur_col)
        cur_max = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    count = 0
                    for left, right, enemy_count in row_list[i]:
                        if left > j:
                            break
                        if left <= j <= right:
                            count += enemy_count
                    for left, right, enemy_count in col_list[j]:
                        if left > i:
                            break
                        if left <= i <= right:
                            count += enemy_count
                    cur_max = max(cur_max, count)
        return cur_max

sol = Solution()
print sol.maxKilledEnemies(["0E00","E0WW","0E00"])
print sol.maxKilledEnemies(["WWWWE","WEEEE", "WE0E0","WEEEE","WWWWW"])