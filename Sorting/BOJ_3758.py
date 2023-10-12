# KCPC, S2, 정렬

from sys import stdin

# 팀 id, 문제번호, 제출되는 시간
T = int(stdin.readline())

for _ in range(T):
    n, k, t, m = map(int, stdin.readline().split())
    # 팀 수, 문제 수, 내 ID, 로그 수

    teams = [[[0]*k, 0, 0] for _ in range(n+1)]     # 점수, 제출 횟수, 제출 시간

    for cnt in range(m):
        i, j, s = map(int,stdin.readline().split())
        # 팀 ID, 문제 번호, 점수
        teams[i][0][j-1] = max(s, teams[i][0][j-1])
        teams[i][1] += 1
        teams[i][2] = cnt+1

    tmp = []

    to = 1
    for team in teams[1:]:
        tmp.append([to, sum(team[0]), team[1],team[2]])
        to += 1

    res = sorted(tmp, key= lambda x : (-x[1], x[2], x[3]))

    cnt = 1
    for i in range(len(res)):
        if res[i][0] == t:
            print(cnt)
            break
        cnt += 1