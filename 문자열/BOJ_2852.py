# NBA 농구, S3, 문자열

from sys import stdin

n = int(stdin.readline())

score = {1: 0, 2: 0}
time = {1: 0, 2: 0}
res = {1: 0, 2: 0}

flag = 0        # 0 = 비김, 1 = 1팀, 2 = 2팀

for _ in range(n):
    team, t = stdin.readline().split()

    team = int(team)
    m, s = map(int, t.split(':'))

    t = m*60 + s

    score[team] += 1

    if flag == 0:       # 비기는 중이었는데 어디하나 골 들어감
        time[team] = t
        flag = team
    elif flag != 0 and score[1] == score[2]:        # 어디하나가 이기고 있었는데 동점됨
        res[flag] += t-time[flag]                   # 이기고 있던 시간을 계산해서 res에 넣어줌
        flag = 0

if flag != 0:
    res[flag] += 60 * 48 - time[flag]       # 경기가 끝날때 동점이 아님

print('{:0>2}:{:0>2}'.format(res[1]//60, res[1]%60))
print('{:0>2}:{:0>2}'.format(res[2]//60, res[2]%60))

