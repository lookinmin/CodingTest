from sys import stdin

n = int(stdin.readline())
# 1 -> 3 -> 5 -> 9 ->  ...
# * 2 - 1?
dp = [0] * 16
dp[0] = 2 # 2*2
dp[1] = 3 # 3*3
dp[2] = 5 # 5*5
for i in range(3, n + 1):
    dp[i] = dp[i-1] * 2 - 1

print(dp[n] ** 2)