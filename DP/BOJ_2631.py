# 줄세우기, G4, DP
# LIS
from sys import stdin

n = int(stdin.readline())
arr = [0]
dp = [1] * (n+1)

for _ in range(n):
    arr.append(int(stdin.readline().rstrip()))

for i in range(1, n+1):
    for j in range(1, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))