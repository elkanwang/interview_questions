# qn4


q = deque()
n = int(raw_input())
for i in range(n):
    ops = raw_input().split()
    # print ops, q
    if ops[0] == "pop":
        q.pop()
        if len(q) == 0:
            print "EMPTY"
        else:
            print q[-1]
    if ops[0] == "push":
        num = int(ops[1])
        q.append(num)
        print q[-1]
    if ops[0] == "inc":
        incVal = int(ops[2])
        incNum = int(ops[1])
        for i in range(incNum):
            q[i] += incVal
        print q[-1]



# q3
# -- candy

# q2 zigzag array


def wiggleArrangeArray(intArr):
    intArr.sort()
    if len(intArr) <2:
        return intArr
    intArr = [intArr[-1]] + intArr[:-1]
    if len(intArr) == 2:
        return intArr
    i = 2
    while i < len(intArr):
        intArr = intArr[:i] + [intArr[-1]] + intArr[i:-1]
        i += 2
    return intArr



# q1 element in bst
