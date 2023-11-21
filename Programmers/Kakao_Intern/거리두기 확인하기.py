from collections import deque


def bfs(graph):
    # 각 P 의 위치를 q에 담고, bfs수행
    start = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(5):
        for j in range(5):
            if graph[i][j] == 'P':
                start.append([i, j])

    for s in start:
        q = deque([s])
        visited = [[-1] * 5 for _ in range(5)]
        # 방문 처리이자 거리
        visited[s[0]][s[1]] = 0

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == -1:
                    if graph[nx][ny] == 'O':
                        q.append([nx, ny])
                        visited[nx][ny] = visited[x][y] + 1
                    if graph[nx][ny] == 'P' and visited[x][y] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    # places의 각 place를 graph로 변환
    for place in places:
        answer.append(bfs(place))
    return answer