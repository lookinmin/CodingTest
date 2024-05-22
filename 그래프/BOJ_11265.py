# 끝나지 않는 파티, G5
from sys import stdin

# 단방향 그래프
# 최단 경로
# 인접 행렬 방식

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j] 
    

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    a = a - 1
    b = b - 1
    if graph[a][b] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")