# 마라톤1, S3, 구현

from sys import stdin
n = int(stdin.readline())
checks = []

for _ in range(n):
    x, y = map(int, stdin.readline().split())
    checks.append([x, y])

total = 0

for i in range(n-1):
    total += abs(checks[i][0] - checks[i+1][0]) + abs(checks[i][1] - checks[i+1][1])

maxDis = 0
for i in range(1, n-1):
    prev_to_mid = abs(checks[i][0]-checks[i-1][0])+abs(checks[i][1]-checks[i-1][1])
    mid_to_end = abs(checks[i+1][0]-checks[i][0])+abs(checks[i+1][1]-checks[i][1])
    prev_to_end = abs(checks[i+1][0]-checks[i-1][0])+abs(checks[i+1][1]-checks[i-1][1])
    val = prev_to_mid + mid_to_end - prev_to_end
    maxDis = max(maxDis, val)

print(total-maxDis)

