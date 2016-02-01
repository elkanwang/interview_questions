data = []
n = int(raw_input())
for i in range(n):
    spell = raw_input().split()
    spell[0] = int(spell[0])
    spell[1] = int(spell[1])
    spell[2] = int(spell[2])
    data.append(spell)

# data = [[2,6,5],[8,9,1],[3,7,2]]
# sorted(data, key=lambda d:d[0])

res = [0]*2000000

for d in data:
    for i in range(int(d[1])):
        res[int(d[0])+i] = max(int(d[2]),res[int(d[0])+i])
cur = 0
ress = []
for i,v in enumerate(res):
    if v != cur:
        ress.append(str(i)+" "+str(v))
        cur = v
print len(ress)
for r in ress:
    print r
# from collections import deque
# slots = []
# for d in data:
#     d = deque([d])
#     while d:
#         d1 = d.pop()
#         print d1, slots
#         for s in slots:
#             if d1[0] <= s[0] and d1[1] >= s[1]:
#                 # cover all
#                 if d1[2] > s[2]:
#                     s[2] = d1[2]
#                 if d1[0] != s[0]:
#                     d.append([d1[0], s[0], d1[2]])
#                 if s[1] != d1[1]:
#                     d.append([s[1], d1[1], d1[2]])
#                 break
#             elif d1[0] >= s[0] and d1[1] <= s[1]:
#                 if d1[2] > s[2]:
#                     d1.append(d1)
#                     slots.append([d1[1], s[1], s[2]])
#                     s[1] = d1[0]
#                 break
#             elif d1[0] <= s[1] and d1[1] >= s[0]:
#                 if d1[2] > s[2]:
#                     slots.append([d1[0], s[1], d[2]])
#                     s[1] = d1[0]
#                 if s[1] != d1[1]:
#                     d.append([s[1], d1[1], d1[2]])
#                 break
#             elif d1[1] <= s[1] and d1[1]>=s[0]:
#                 if d1[2] > s[2]:
#                     slots.append([s[0], d1[1], d[2]])
#                     s[0] = d1[1]
#                 if d1[0] != s[0]:
#                     d.append([d1[0], s[0], d1[2]])
#                 break
#         slots.append(d1)
# print slots
