# 합 분해, G5, DP-수학
# 0 ~ n까지 정수 k 개 더해서 합이 n 되는 경우의 수 구하기
# 1+2, 2+1은 다른 경우, 1+1+1 가능

# n == 1, 경우의 수 = k개
# k == 1, 경우의 수 = 1개
# k == 2, 경우의 수 = k+1개
# k == 3, dp[i][j] = dp[i-1][j] + dp[i][j-1]


from sys import stdin
n, k = map(int,stdin.readline().split())

dp = [[0] * 201 for _ in range(201)]
for i in range(201):
    dp[1][i] = 1        # k == 1, 경우의 수 = 1개
    dp[2][1] = i+1      # k == 2, 경우의 수 = k+1개

for i in range(2, 201):
    dp[i][1] = i        # n == 1, 경우의 수 = k개
    for j in range(2, 201):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

print(dp[k][n])
