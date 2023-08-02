# 게임 개발, G3, 그래프-위상정렬

from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = [[] for _ in range(n+1)]
inDegree = [0] * (n+1)      # 각 노드 진입 차수
cost = [0] * (n+1)          # 각 건물 지을때 걸리는 시간

# 각 건물 완성에 대한 최소시간 출력

for i in range(1, n+1):
    tmp = list(map(int, stdin.readline().split()))[:-1]
    cost[i] = tmp[0]
    for j in tmp[1:]:       # 간선 연결
        graph[j].append(i)
    inDegree[i] += len(tmp[1:])     # 각 노드에 대한 진입 차수

def topology_sort():        # 위상정렬
    res = [0] *(n+1)
    q = deque()

    for i in range(1, n+1):
        if inDegree[i] == 0:        # 차수가 1이면 바로 진입가능하니까
            q.append(i)             # 큐에 넣어준다

    while q:
        now = q.popleft()       # 현재 위치한 노드
        res[now] += cost[now]   # 현재 위치한 노드를 짓는데 걸리는 시간

        for v in graph[now]:    # 지금거 짓고 지을 수 있는 건물(연결된거)
            inDegree[v] -= 1
            res[v] = max(res[v], res[now])  # v를 짓는데 걸리는 시간을 현재 건물을 짓고 나서로 갱신
            if inDegree[v] == 0:
                q.append(v)
    return res

ans = topology_sort()
for i in range(1, n+1):
    print(ans[i])

