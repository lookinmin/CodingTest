# 1,2,3 더하기 3, 실버2, DP
# 정수 n을 1, 2, 3의 합으로 나타내는 방법의 수

# 점화식 -> dp[n] = dp[n-3] + dp[n-2] + dp[n-1]
from sys import stdin
t = int(stdin.readline())

dp = [0 for _ in range(1000001)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 1000001):
    dp[i] = dp[i-1] % 1000000009  + dp[i-2] % 1000000009  + dp[i-3] % 1000000009

for _ in range(t):
    n = int(stdin.readline())
    print(dp[n] % 1000000009 )