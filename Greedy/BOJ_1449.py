# 수리공 항승, 실버3, 그리디
from sys import stdin
import math
n, l = map(int,stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

arr.sort()

start = arr[0]
cnt = 1

for i in arr[1:]:
    if i in range(start, start + l):
        continue
    else:
        start = i
        cnt += 1

print(cnt)