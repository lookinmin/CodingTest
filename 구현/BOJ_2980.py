# 도로와 신호등, 실버4, 구현-시뮬레이션

from sys import stdin
n,l = map(int, stdin.readline().split())
pos = 0
res = 0
for _ in range(n):
    d, r, g= map(int, stdin.readline().split())
    res += (d - pos)
    pos = d
    if res % (r + g) <= r:
        res += (r - (res%(r+g)))

res += (l - pos)
print(res)