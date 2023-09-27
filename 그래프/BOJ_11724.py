# 연결 요소의 개수, S2, 그래프 - connected component 찾기
# BFS

from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)

for i in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u] += [v]
    graph[v] += [u]

# 여기까지 그래프에 값 넣고 BFS 함수 짜기

cnt = 0

for i in range(1, n+1):
    if visited[i] == 0:         # 각 노드를 방문하지 않았다면
        if not graph[i]:        # 해당 노드가 이어진 vertex가 없다면
            cnt += 1            # 끊어진거니까 cnt + 1
        else:                   # 이어진 vertex 있으면
            bfs(i)              # BFS 돌리고
            cnt += 1            # BFS 한번 다 돌았으면 더이상 이어진거 없으므로 + 1
                                # BFS를 다 돌린 순간 해당 노드들은 visited == 1 이 되어 30번째 줄 if문에 걸리지 않는다.
print(cnt)

