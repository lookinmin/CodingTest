from collections import deque

def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    dist = [[int(1e9)] * m for _ in range(n)]


    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # start = 1,1
    # end = n, m

    def bfs():
        q = deque()
        q.append([0,0,1])   # x, y, cnt
        visited[0][0] = 1
        dist[0][0] = 1

        while q:
            x, y, cnt = q.popleft()

            if x == n-1 and y == m-1:
                return dist[n-1][m-1]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                    if maps[nx][ny] == 1:
                        q.append([nx,ny, cnt + 1])
                        visited[nx][ny] = 1
                        dist[nx][ny] = min(cnt + 1, dist[nx][ny])


    answer = bfs()

    return answer if answer is not None else -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))