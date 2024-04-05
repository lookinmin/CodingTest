# 놀이공원, S3
from sys import stdin
n = int(stdin.readline())
# 1000 ~ 2200
arr = [[600, 600], [1320, 1320]]
for _ in range(n):
    start, end = stdin.readline().split()
    start = int(start[:2]) * 60 + int(start[2:]) - 10
    end = int(end[:2]) * 60 + int(end[2:]) + 10
    arr.append([start, end])

arr.sort()

res = 0
last = 600
for s, e in arr:
    res = max(res, s - last)
    last = max(last, e)
print(res)