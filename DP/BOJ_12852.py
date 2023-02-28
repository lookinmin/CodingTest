# 1로 만들기2, S1, DP

from sys import stdin

# if X%3 == 0, // 3
# if X%2 == 0, // 2
# -1

n = int(input())
# ai = min(ai-1,ai/2, ai/3, ai/5) + 1
dp = [i for i in range(n+1)]
dp[1] = 0
res = [i for i in range(n+1)]
res[1] = 0

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    res[i] = i-1
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        res[i] = i // 3

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i//2] + 1
        res[i] = i // 2


print(dp[n])
print(n, end=" ")

back_num = n
while res[back_num] != 0:
    print(res[back_num], end=" ")
    back_num = res[back_num]

