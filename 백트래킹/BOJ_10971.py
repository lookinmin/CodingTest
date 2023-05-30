# 외판원 순회2, S2, 완탐

from sys import stdin

n = int(stdin.readline())
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

# 가장 기본적인 형태의 TSP
# dfs 해결

visited = [0] * n       # 각 노드에 대해 방문 처리
res = int(1e9)

add = 0

def dfs(node, cnt, cost):
    global res

    if cnt == n:              # n개의 노드를 모두 탐색했다면
        if graph[node][0] != 0:
            res = min(res, cost + graph[node][0])
        return

    for i in range(1, n):       # 해당 노드랑 연결된 다른 노드들에 대해 탐색
        if graph[node][i] != 0 and not visited[i]:
            visited[i] = 1
            dfs(i, cnt + 1, cost + graph[node][i])
            visited[i] = 0

dfs(0, 1, 0)        # 시작 cost는 0, 방문 시작 노드는 0번부터, 시작부터 하나 방문하니까 x는 1부터
print(res)