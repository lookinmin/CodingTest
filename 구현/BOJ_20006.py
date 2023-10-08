# 랭킹전 대기열, S2, 구현

from sys import stdin

p, m = map(int, stdin.readline().split())

rooms = []

for _ in range(p):
    level, name = map(str, stdin.readline().split())
    level = int(level)

    flag = False

    for room in rooms:
        if len(room) < m and (room[0][0] + 10 >= level >= room[0][0] - 10):
            room.append((level, name))
            flag = True
            break

    if not flag:
        rooms.append([(level, name)])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    room.sort(key= lambda x : x[1])
    for l, n in room:
        print(l, n)




# people = []
#
# for _ in range(p):
#     level, name = map(str, stdin.readline().split())
#     people.append([int(level), name])
#
# for lv, name in people:
#     flag = 0
#
#     for i in range(len(room)):
#         if len(room[i][1]) == m:        # 해당 방의 정원이 max
#             continue
#
#         if room[i][0] + 10 >= lv >= room[i][0] - 10:
#             flag = 1
#             room[i][1].append([lv, name])
#             break
#
#     if not flag:
#         room.append([lv, [[lv ,name]]])
#
#
# for i in range(len(room)):
#     if len(room[i][1]) == m:
#         print("Started!")
#         tmp = sorted(room[i][1], key= lambda x : x[1])
#         for j in range(m):
#             print(*tmp[j])
#     else:
#         print("Waiting!")
#         tmp = sorted(room[i][1], key=lambda x: x[1])
#         for j in range(m):
#             print(*tmp[j])