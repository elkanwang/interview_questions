# Complete the function below.


def checkIllumination(n, lamps, queries):
    board = [[set() for j in range(n)] for i in range(n)]
    for index, lamp in enumerate(lamps):
        lamps[index] = (lamp[0], lamp[1])
    # print lamps
    lamps = set(lamps)

    def lit(board, lamp_x, lamp_y, n):
        for i in range(n):
            board[lamp_x][i].add((lamp_x, lamp_y))
            board[i][lamp_y].add((lamp_x, lamp_y))
        new_lamp_x, new_lamp_y = lamp_x, lamp_y
        while 0 <= new_lamp_x < n and 0 <= new_lamp_y < n:
            board[new_lamp_x][new_lamp_y].add((lamp_x, lamp_y))
            new_lamp_x += 1
            new_lamp_y += 1
        new_lamp_x, new_lamp_y = lamp_x, lamp_y
        while 0 <= new_lamp_x < n and 0 <= new_lamp_y < n:
            board[new_lamp_x][new_lamp_y].add((lamp_x, lamp_y))
            new_lamp_x -= 1
            new_lamp_y -= 1
        new_lamp_x, new_lamp_y = lamp_x, lamp_y
        while 0 <= new_lamp_x < n and 0 <= new_lamp_y < n:
            board[new_lamp_x][new_lamp_y].add((lamp_x, lamp_y))
            new_lamp_x += 1
            new_lamp_y -= 1
        new_lamp_x, new_lamp_y = lamp_x, lamp_y
        while 0 <= new_lamp_x < n and 0 <= new_lamp_y < n:
            board[new_lamp_x][new_lamp_y].add((lamp_x, lamp_y))
            new_lamp_x -= 1
            new_lamp_y += 1

    for lamp_x, lamp_y in lamps:
        lit(board, lamp_x, lamp_y, n)
    # for i in range(n):
    #     for j in range(n):
            # print board[i][j]
    result = []
    for query_x, query_y in queries:
        if query_x >= n or query_y >= n:
            result.append('DARK')
            continue
        lamp_included = set()
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                new_query_x, new_query_y = query_x + x, query_y + y
                if 0 <= new_query_x < n and 0 <= new_query_y < n:
                    if (new_query_x, new_query_y) in lamps:
                        lamp_included.add((new_query_x, new_query_y))
        # print board[query_x][query_y], lamp_included, board[query_x][query_y] - lamp_included
        # print query_x, query_y
        result.append('LIGHT' if board[query_x][query_y] - lamp_included else 'DARK')
    return result


_n = int(raw_input());

_lamps_rows = 0
_lamps_cols = 0
_lamps_rows = int(raw_input())
_lamps_cols = int(raw_input())

_lamps = []
for _lamps_i in xrange(_lamps_rows):
    _lamps_temp = map(int, raw_input().strip().split(' '))
    _lamps.append(_lamps_temp)

_queries_rows = 0
_queries_cols = 0
_queries_rows = int(raw_input())
_queries_cols = int(raw_input())

_queries = []
for _queries_i in xrange(_queries_rows):
    _queries_temp = map(int, raw_input().strip().split(' '))
    _queries.append(_queries_temp)

res = checkIllumination(_n, _lamps, _queries);
for res_cur in res:
    print(str(res_cur))
