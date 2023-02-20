# 공통 부분 문자열, G5, DP - LCS

from sys import stdin
a = stdin.readline().strip()
b = stdin.readline().strip()

# LCS=[[0]*4001 for _ in range(4001)]
LCS=[[0]*(len(b)+1) for _ in range(len(a)+1)]
ans = 0

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
            ans = max(LCS[i][j], ans)

print(ans)