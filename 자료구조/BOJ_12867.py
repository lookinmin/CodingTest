# N차원 여행, S2
from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
travel = list(map(int, stdin.readline().split()))
op = list(map(str, stdin.readline().rstrip()))

flag = True
path = [{}]
now = dict()

for i in range(m):
    now[travel[i]] = now.get(travel[i],0) + (1 if op[i] == '+' else -1)

    if now[travel[i]] == 0:
        del now[travel[i]]

    for cmp in path:
        if now.items() == cmp.items():
            print(0)
            exit()

    print("현재 방문: {}".format(now))

    path.append(now.copy())

if now == {}:
    print(0)
else:
    print(1)