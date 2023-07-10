# LCS, G5, 파이썬

from sys import stdin

a1 = list(stdin.readline().rstrip())
a2 = list(stdin.readline().rstrip())

dp = [0] * len(a2)


for i in range(len(a1)):
    cnt = 0     # 누적변수
    for j in range(len(a2)):
        if cnt < dp[j]:
            cnt = dp[j]
        elif a1[i] == a2[j]:
            dp[j] = cnt + 1

print(max(dp))
