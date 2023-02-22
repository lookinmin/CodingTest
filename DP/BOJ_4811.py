# 알약, G5, DP

from sys import stdin
dp = [[0]*31 for _ in range(31)]
# dp[i][j]에서 i = w의 수, j = h의 수, dp[i][j] == w i개, h j개로 만들 수 있는 경우의 수

for j in range(1, 31):
    dp[0][j] = 1        # 초기화

for i in range(1, 31):
    for j in range(30):
        if j == 0:      # h=0개 일때, w하나먹으면 h+=1
            dp[i][j] = dp[i-1][j+1]
        else:           # h가 하나라도 있으면, h먹을때 + w먹을때 2가지 경우의 수
            dp[i][j] = dp[i-1][j+1] + dp[i][j-1]

while 1:
    n = int(stdin.readline())
    if n == 0:
        break
    print(dp[n][0])

