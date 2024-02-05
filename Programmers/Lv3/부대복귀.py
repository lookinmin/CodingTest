from collections import deque

def solution(n, roads, sources, end):
    graph = [[] for _ in range(n + 1)]

    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])

    dist = [-1] * (n + 1)

    # 생각을 바꿔보자
    # destination -> start로 가도 된다.

    def bfs():
        q = deque()
        dist[end] = 0
        q.append(end)

        while q:
            now = q.popleft()

            for v in graph[now]:
                if dist[v] == -1:
                    dist[v] = dist[now] + 1
                    q.append(v)

    bfs()
    answer = []
    for source in sources:
        answer.append(dist[source])

    return answer