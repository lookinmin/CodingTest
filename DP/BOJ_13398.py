# 연속합 2, G5, DP

from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

dp = [[0] * n for _ in range(2)]        #dp[0][i] = 제거X 수열, dp[1][i] = 제거O 수열
dp[0][0] = arr[0]
dp[1][0] = -1000

for i in range(1, n):
    dp[0][i] = max(dp[0][i-1] + arr[i], arr[i])     # 이전꺼를 더한값 or 새로 가는거(음수일때)
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])     # 지금꺼를 버리기 or 계속 더해나가기

tmp1, tmp2  = max(dp[0]), max(dp[1])
print(max(tmp1, tmp2))


