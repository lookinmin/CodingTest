# 걸그룹 마스터 준석이, S3, 해시

from sys import stdin

N, M = map(int, stdin.readline().split())

group = {}
for _ in range(N):
    team = stdin.readline().rstrip()
    group[team] = []
    num = int(stdin.readline())
    for _ in range(num):
        group[team].append(stdin.readline().rstrip())

for _ in range(M):
    sub = stdin.readline().rstrip()
    num = int(stdin.readline())
    if num == 0:
        for w in sorted(group[sub]):
            print(w)
    else:
        for team in group.items():
            if sub in team[1]:
                print(team[0])