# 서강그라운드, G4, 플로이드 워셜

from sys import stdin

INF = int(1e9)

n, m, r = map(int, stdin.readline().split())
# m 은 범위 limit

items = [-1] + list(map(int, stdin.readline().split()))
dist = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0          # 나 자신에게 가는 거리는 0으로 초기화

for _ in range(r):
    a, b, l = map(int, stdin.readline().split())
    dist[a][b] = l
    dist[b][a] = l

for i in range(1, n+1):             # 플로이드 워셜 식 외우기 i -> j -> k
    for j in range(1, n+1):
        for k in range(1, n+1):     # jk > ji + ik
            if dist[j][k] > dist[j][i] + dist[i][k]:
                dist[j][k] = dist[j][i] + dist[i][k]

res = 0

for i in range(1, n+1):
    tmp = 0
    for j in range(1, n+1):
        if dist[i][j] <= m:     # 범위 안, 갈 수 있음
            tmp += items[j]
    res = max(res, tmp)

print(res)