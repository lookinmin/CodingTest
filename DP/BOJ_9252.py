# LCS2, G4, DP-LCS
from sys import stdin

s1 = [0]+list(stdin.readline().strip())       # 1번째 인덱스부터
s2 = [0]+list(stdin.readline().strip())
# 길이만 찾아내기
# dp = [0] * max(len(s1), len(s2))
# res = ""
#
# for i in range(len(s1)):
#     cnt = 0
#     for j in range(len(s2)):
#         if cnt < dp[j]:
#             cnt = dp[j]
#         elif s1[i] == s2[j]:
#             dp[j] = cnt + 1
#             print(dp)
#
# print(max(dp))

dp = [[""] * len(s2) for _ in range(len(s1))]

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + s1[i]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

res = dp[len(s1)-1][len(s2)-1]
print(len(res))
print(res)


