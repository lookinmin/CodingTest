# 점프 점프, S2, DP
# https://kau-algorithm.tistory.com/188 참고
from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
dp = [n+1] * n
dp[0] = 0

for i in range(n):
    for j in range(1, arr[i] + 1):
        if i + j < n:
            dp[i+j] = min(dp[i] + 1, dp[i + j])

if dp[n-1]==n + 1:
    print(-1)
else:
    print(dp[n-1])