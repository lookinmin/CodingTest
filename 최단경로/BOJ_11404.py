# 플로이드, G4, 플로이드-워셜

from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
INF = int(1e9)
graph = [[INF] * n for _ in range(n)]

for i in range(m):
    a, b, c = map(int, stdin.readline().split())
    if graph[a-1][b-1] > c:
        graph[a-1][b-1] = c

# 플로이드-워셜

for k in range(n):     # 경로 for문
    for i in range(n):
        for j in range(n):
            if i != j and graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()