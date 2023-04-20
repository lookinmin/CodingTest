# 2xn 타일링 2, S3, DP - DP 감 다시 잡기
# 지난 문제에 비해 2*2 타일이 추가됨

n = int(input())
dp = [0] * 1001

dp[1] = 1
dp[2] = 3
dp[3] = 5
dp[4] = 11

for i in range(5, n+1):
    dp[i] = dp[i-2] * 2 + dp[i-1]

print(dp[n] % 10007)