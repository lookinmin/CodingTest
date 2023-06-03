# 키 순서, G4, 플로이드 워셜

from sys import stdin

n, m = map(int, stdin.readline().split())
graph =[[0] * (n+1) for _ in range(n+1)]

# 자신이 갈 수 있는 노드 = 자기보다 작은 사람
# 자기에게 오는 경로가 있는 사람 = 자기보다 큰 사람
# 이 둘의 합이 n-1 == 자신의 순서를 알 수 있음

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

res = 0

for i in range(1, n+1):
    know = 0
    for j in range(1, n+1):
        know += graph[i][j] + graph[j][i]       # 자기보다 큰사람 + 자기보다 작은사람

    if know == n-1:
        res += 1

print(res)