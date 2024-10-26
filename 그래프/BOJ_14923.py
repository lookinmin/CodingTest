from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
sx, sy = map(int, stdin.readline().split())
sx -= 1
sy -= 1

ex, ey = map(int, stdin.readline().split())
ex -= 1
ey -= 1

graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]  # 3차원 visited 배열 사용

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque([(sx, sy, 0, 0)])  # (현재 x, y, 벽 부순 횟수, 이동 거리)
    visited[sx][sy][0] = True
    
    while q:
        x, y, wall_broken, dist = q.popleft()
        
        if x == ex and y == ey:
            return dist
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and wall_broken == 0 and not visited[nx][ny][1]:
                    # 벽이 있고 아직 벽을 부수지 않은 상태에서 벽을 부수는 경우
                    visited[nx][ny][1] = True
                    q.append((nx, ny, 1, dist + 1))
                elif graph[nx][ny] == 0 and not visited[nx][ny][wall_broken]:
                    # 빈 칸으로 이동하는 경우
                    visited[nx][ny][wall_broken] = True
                    q.append((nx, ny, wall_broken, dist + 1))
    
    return -1

res = bfs()
print(res)
