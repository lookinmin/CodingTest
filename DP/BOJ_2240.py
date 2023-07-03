# 자두나무, G5, DP
# 나무는 두개밖에 없다
from sys import stdin

t, w = map(int, stdin.readline().split())
prum = [0]
for _ in range(t):
    prum.append(int(stdin.readline().rstrip()))

# 사람의 이동횟수가 홀수다 -> 2번 나무
# 짝수다 -> 1번 나무

dp = [[0] * (w+1) for _ in range(t+1)]

for i in range(t+1):

    # 1번에서 움직이지 않음
    if prum[i] == 1:
        dp[i][0] = dp[i-1][0] + 1       # 1번나무에서 떨어지는거 하나 추가

    else:
        dp[i][0] = dp[i-1][0]           # 나머지 나무에서는 못받음

    for j in range(1, w+1):

        if prum[i] == 2 and j % 2 == 1:         # 2번에서 떨어지고 내가 2번에 있음
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
            # 움직여서 먹을건지 아님 기존자리 고수할 건지

        elif prum[i] == 1 and j % 2 == 0:       # 1번에서 떨어지고 내가 1번에 있음
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        else:       # 현재 나무와 자두가 떨어지는 나무의 위치가 다름
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[t]))