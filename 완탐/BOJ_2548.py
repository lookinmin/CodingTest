# 대표 자연수, S3
from sys import stdin
n = int(stdin.readline())
arr = sorted(list(map(int, stdin.readline().split())), reverse=True)

INF = int(1e9)
res = [INF, INF]
for num in arr:
    val = 0

    for n in arr:
        val += abs(num - n)

    if val <= res[0]:
        res[0] = val
        res[1] = num

print(res[1])