from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    MAX_SIZE = 102
    graph = [[0] * MAX_SIZE for _ in range(MAX_SIZE)]
    visited = [[-1] * MAX_SIZE for _ in range(MAX_SIZE)]
    
    # 두 배로 확장하여 사각형 채우기
    for sx, sy, ex, ey in rectangle:
        for x in range(sx * 2, ex * 2 + 1):
            for y in range(sy * 2, ey * 2 + 1):
                graph[x][y] = 1
    
    # 테두리의 점이라면 True, 아니면 False
    def is_boundary(x, y):
        dx = [-1, 1, 0, 0, -1, 1, -1, 1]
        dy = [0, 0, -1, 1, -1, -1, 1, 1]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < MAX_SIZE and 0 <= ny < MAX_SIZE:
                if graph[nx][ny] == 0:
                    return True
        return False

    def bfs():
        q = deque()
        q.append([characterX * 2, characterY * 2])
        visited[characterX * 2][characterY * 2] = 0
        
        # 4방향 탐색
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        while q:
            x, y = q.popleft()
            
            if x == itemX * 2 and y == itemY * 2:
                return visited[x][y] // 2

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < MAX_SIZE and 0 <= ny < MAX_SIZE and visited[nx][ny] == -1 and graph[nx][ny] == 1 and is_boundary(nx, ny):
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])
        return -1

    return bfs()
