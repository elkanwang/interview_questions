def  isFrenemy(n, frenemy, x, y, relation):
    if len(relation) < 1:
        return 1
    level = set()
    level.add(x)
    while len(relation)>0:
        r = relation[0]
        newLevel = set()
        for i in level:
            for j in range(n):
                if frenemy[i][j] == r:
                    newLevel.add(j)
        relation = relation[1:]
        level = newLevel
    return y in level

print isFrenemy(2, ["-F","F-"], 0, 1, "F")
