# 요세푸스 문제, S4, 구현

from sys import stdin

n, k = map(int, stdin.readline().split())

arr = []
for i in range(1, n+1):
    arr.append(i)
t = 0
res = []
for i in range(n):
    t += k-1
    if t >= len(arr):
        t %= len(arr)
    res.append(str(arr.pop(t)))

print("<",", ".join(res)[:],">", sep='')

