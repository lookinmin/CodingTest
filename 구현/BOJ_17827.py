# S2, 달팽이 리스트
from sys import stdin

n, m, v = map(int, stdin.readline().split())
v -= 1
graph = list(map(int, stdin.readline().split()))

cycle_length = n - v
res = []

for _ in range(m):
    k = int(input())
    if k < n:
        res.append(graph[k])
    else:
        num = (k - v) % cycle_length
        res.append(graph[v + num])

for num in res:
    print(num)
