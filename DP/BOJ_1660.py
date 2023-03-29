# 캡틴 이다솜, S1, DP

from sys import stdin

n = int(stdin.readline().rstrip())
balls = []      # 만들 수 있는 사면체의 수
ball = 0

for i in range(1, 300001):
    ball += (i * (i+1)) // 2        # 공 증가 점화식 1->3->6 ...
    balls.append(ball)

    if balls[-1] >= n:          # n개 이상의 공으로 모여있는 사면체는 필요없다 (무조건 1개니까)
        break

INF = int(1e9)
dp = [INF] * (n+1)

for i in range(1, n+1):
    for j in balls:
        if j == i:      # 현재 뭉쳐있는 사면체의 수 = 대포알의 수
            dp[i] = 1
            break
        if j > i:       # 대포알 수로 사면체를 만들 수 없음
            break
        dp[i] = min(dp[i], dp[i-j] + 1)     # 현재 대포알의 수로 만들 수 있는 사면체 확인

print(dp[n])



