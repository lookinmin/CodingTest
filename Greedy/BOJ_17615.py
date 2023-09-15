# 볼 모으기, S1, 그리디

from sys import stdin
# 오른쪽으로만 이동한다 생각하자

n = int(stdin.readline())
balls = list(stdin.readline().rstrip())

Rcnt = balls.count('R')
Bcnt = balls.count('B')

res = min(Rcnt, Bcnt)       # 더 적은 수의 공이 답


# 앞에서부터 모으기
cnt = 0

for i in range(n):
    if balls[i] != balls[0]:
        break
    cnt += 1

if balls[0] == 'R':
    res = min(res, Rcnt - cnt)
else:
    res = min(res, Bcnt - cnt)

# 뒤에서부터 모으기

cnt = 0

for i in range(n-1, -1, -1):
    if balls[i] != balls[-1]:
        break
    cnt += 1

if balls[-1] == 'R':
    res = min(res, Rcnt - cnt)
else:
    res = min(res, Bcnt - cnt)

print(res)