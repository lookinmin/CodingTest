# 병사 배치하기,S2,DP-LIS

from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] < arr[j]:     # 현재 위치보다 이전 값이 더 큰가
            dp[i] = max(dp[i], dp[j] + 1)   # 더 크면 이전 j까지의 dp 값보다 + 1

print(len(arr) - max(dp))



