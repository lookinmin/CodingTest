# 상자 넣기, 실버2, DP

from sys import stdin
n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):          # 이게 언제는 i까지, 언제는 n까지 -> 차이를 어떻게 구분?
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))