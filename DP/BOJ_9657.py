# 돌 게임3, S3, DP
from sys import stdin
# 돌 1, 3, 4
n = int(stdin.readline())
# 1 상근 0 창영
# 남은 돌이 1, 3, 4 -> 내가 무조건 이김(상근)
dp = [-1, 1, 0, 1, 1] + [-1]*(n-4)

if n <= 4:
    pass
else:
    for i in range(5, n+1):
        if 0 in [dp[i-1], dp[i-3], dp[i-4]]:
            dp[i] = 1
        else:
            dp[i] = 0

if dp[n] == 1:
    print("SK")
else:
    print("CY")