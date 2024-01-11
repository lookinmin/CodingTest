from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])

    # S -> L -> E

    def bfs(start, end):
        q = deque()
        visited = [[0] * m for _ in range(n)]
        q.append(start)

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])

        return visited[end[0]][end[1]]

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                mid = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)

    startTomid = bfs(start, mid)
    midToend = bfs(mid, end)

    return startTomid + midToend if startTomid and midToend else -1