from collections import deque

def bfs(graph, u):
    n = len(graph)
    INF = int(1e9)
    visited = [[INF] * n for _ in range(n)]
    q = deque()
    visited[0][0] = 0
    q.append([0,0,u,0])     # x, y, dir, cost

    # 0 동 1 남 2 서 3 북
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while q:
        x, y, dir, cost = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                # 직진일 때
                if i == dir:
                    nc = cost + 100
                # 곡선일때
                else:
                    nc = cost + 600

                if nc < visited[nx][ny]:
                    visited[nx][ny] = nc
                    q.append([nx, ny, i, nc])

    return visited[-1][-1]

def solution(board):
    answer = 0
    # 시작은 0,0
    # 끝은 n-1,n-1

    answer = min(bfs(board, 0), bfs(board, 1))
    return answer

