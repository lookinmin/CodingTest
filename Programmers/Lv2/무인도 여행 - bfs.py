from collections import deque


def solution(maps):
    answer = []

    k = len(maps[0])  # 가로
    k2 = len(maps)  # 세로

    visited = [[0] * k for _ in range(k2)]

    def bfs(a, b):
        q = deque()
        q.append([a, b])
        visited[a][b] = 1
        value = int(maps[a][b])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < k2 and 0 <= ny < k and not visited[nx][ny] and maps[nx][ny] != 'X':
                    value += int(maps[nx][ny])
                    visited[nx][ny] = 1
                    q.append([nx, ny])
        return value

    for i in range(k2):
        for j in range(k):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(i, j))
    if len(answer):
        answer.sort()
        return answer
    else:
        return [-1]
