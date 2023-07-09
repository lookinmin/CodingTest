# 저울, G4, 플로이드-워셜

from sys import stdin

INF = int(1e9)
n = int(stdin.readline())
m = int(stdin.readline())

graph = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):         # 내가 나한테 접근
    graph[i][i] = 1

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a][b] = 1

for k in range(1 ,n + 1):
    for i in range(1, n + 1):
        for j in range(1 ,n + 1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(1 ,n + 1):
    cnt = 0
    for j in range(1, n+1):
        if graph[i][j] == 0 and graph[j][i] == 0:
            cnt += 1

    print(cnt)
