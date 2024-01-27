from collections import deque
def solution(board):
    answer = 0

    n = len(board)
    m = len(board[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(a, b):
        q = deque()
        q.append([a, b])
        visited = [[0] * m for _ in range(n)]
        visited[a][b] = 1

        while q:
            x, y = q.popleft()

            if board[x][y] == 'G':
                return visited[x][y]

            for i in range(4):
                nx = x
                ny = y

                while 1:
                    nx = nx + dx[i]
                    ny = ny + dy[i]  # 해당 방향 직진
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 'D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break  # 벽이나 장애물에 닿은 만큼 움직임, 마지막 한칸은 빼줘야함.
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                if not visited[nx][ny]:  # 결국 최종적으로 움직인 부분에서 visited를 올린다.
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])
        return -1

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                answer = bfs(i, j)

    return answer - 1 if answer > 0 else -1