def langtonsAnt(direction, steps):
    dircMap = {'left':'<', 'right':'>', 'up':'^', 'down':'v'}
    blackCellList = set()
    x = 0
    y = 0
    # board[x][y] = direction
    for i in range(steps):
        if (x,y) in blackCellList:
            color = '#'
        else:
            color = '.'
        if color == '.': # white cell
            if direction == "left":
                direction = "up"
            elif direction == "up":
                direction = "right"
            elif direction == "right":
                direction = "down"
            else:
                direction = "left"
            blackCellList.add((x,y))
        else: # black cell
            if direction == "left":
                direction = "down"
            elif direction == "down":
                direction = "right"
            elif direction == "right":
                direction = "up"
            else:
                direction = "left"
            blackCellList.remove((x,y))
        if direction == "left":
            y -= 1
        elif direction == "up":
            x -=1
        elif direction == "right":
            y += 1
        else:
            x += 1
    x1 = min(min(blackCellList,key=lambda x:x[0])[0],x)
    x2 = max(max(blackCellList,key=lambda x:x[0])[0],x)
    y1 = min(min(blackCellList,key=lambda x:x[1])[1],y)
    y2 = max(max(blackCellList,key=lambda x:x[1])[1],y)
    for m in range(x1, x2+1):
        row = []
        for n in range(y1, y2+1):
            if (m,n) == (x,y):
                row.append(dircMap[direction])
            elif (m,n) in blackCellList:
                row.append('#')
            else:
                row.append('.')
        print ''.join(row)


langtonsAnt('left', 386)
