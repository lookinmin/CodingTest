# 학교 대표

from sys import stdin

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
tmp = arr[k-1]
cnt = 0
for i in arr:
    if i >= tmp and i != 0:
       cnt += 1

print(cnt)
