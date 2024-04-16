# 물 주기, S3
from sys import stdin

n, k, a, b = map(int, stdin.readline().split())
day = 0

arr = [k] * n
loca = 0

while 0 not in arr:
    loca = arr.index(min(arr))
    for i in range(a):
        arr[loca + i] += b

    for i in range(n):
        arr[i] -= 1

    day += 1

print(day)