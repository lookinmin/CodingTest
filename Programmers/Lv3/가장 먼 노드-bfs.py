from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    dist = [int(1e9)] * (n+1)

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    # 1번 노드가 시작임

    def bfs(s):
        q = deque()
        q.append([s,0])
        visited[s] = 1
        dist[s] = 0

        while q:
            node, depth = q.popleft()
            for v in graph[node]:
                if visited[v] == 0:
                    visited[v] = 1
                    q.append([v, depth + 1])
                    dist[v] = min(dist[v], depth + 1)

    bfs(1)

    maxDist = max(dist[1:])

    for i in range(1, n+1):
        if dist[i] == maxDist:
            answer += 1
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))