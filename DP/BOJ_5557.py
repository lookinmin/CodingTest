# 1학년, G5, DP

from sys import stdin
# 계산하면서 값이 0~20사이여야함

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
dp = [[0] * 21 for _ in range(n)]
# 행이 0~20, 열이 n개 있는 dp 테이블 생성

dp[0][arr[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        if dp[i-1][j]:      # 이전에 계산이 가능했던 행만 계산
            if 0<=j+arr[i]<=20:
                dp[i][j+arr[i]] += dp[i-1][j]
            if 0 <= j - arr[i] <= 20:
                dp[i][j - arr[i]] += dp[i - 1][j]

print(dp[n-2][arr[-1]])     # 입력 수의 마지막 숫자와 일치하는 경우의 수

