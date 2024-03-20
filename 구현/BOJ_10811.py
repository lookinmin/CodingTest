# 바구니 뒤집기
from sys import stdin

n, m = map(int, stdin.readline().split())
arr = [i for i in range(1, n + 1)]

for _ in range(m):
    s, e = map(int, stdin.readline().split())
    s, e = s-1, e-1
    arr[s : e + 1] = arr[s : e + 1][::-1]

print(*arr)