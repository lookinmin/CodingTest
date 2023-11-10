# 운동, G4, 최단거리 - 플로이드

from sys import stdin

# 단방향
# 사이클을 이루는 도로의 길이의 합이 최소

v, e = map(int, stdin.readline().split())
INF = int(1e9)
graph = [[INF] * (v+1) for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    graph[a][b] = c

for k in range(1, v+1):     # K는 경유지
    for i in range(1, v+1):     # i는 출발지
        for j in range(1, v+1): # j는 도착지
            # i->k->j와 i->j를 비교
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

res = INF

for i in range(1, v+1):
    res = min(res, graph[i][i])     # 사이클 확인

print(-1 if res == INF else res)

