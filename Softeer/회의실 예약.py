from sys import stdin

n, m = map(int, stdin.readline().split())
room = {}
for _ in range(n):
    name = stdin.readline().rstrip()
    room[name] = [0] * 18 + [1]

for _ in range(m):
    r, s, t = stdin.readline().split()
    s, t = int(s), int(t)
    for i in range(s, t):
        room[r][i] = 1

sorted_room = sorted(room.items())

for i in range(len(sorted_room)):
    print("Room {}:".format(sorted_room[i][0]))
    if 0 not in sorted_room[i][1][9:19]:
        print("Not available")
    else:
        cnt = 0
        flag = False
        words = ''
        for j in range(9, 19):
            if sorted_room[i][1][j] == 0 and flag == False:
                words += "{:02d}".format(j)
                flag = True
            elif sorted_room[i][1][j] == 1 and flag:
                words += "-{:02d} ".format(j)
                cnt += 1
                flag = False
            if flag and j == 18:
                cnt += 1
                words += "-18 "
        print("{} available:".format(cnt))
        for w in words.strip().split(' '):
            print(w)

    if i != len(sorted_room) - 1:
        print("-----")