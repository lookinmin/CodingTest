from sys import stdin
from itertools import product

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(path, x, y, routes):
    if len(path) == 4:
        routes.append(path[:])
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in path:
            path.append((nx, ny))
            dfs(path, nx, ny, routes)
            path.pop()

def get_total_fruits(routes):
    result = 0
    visited = set()
    for route in routes:
        for x, y in route:
            if (x, y) in visited:
                return 0  # 경로가 겹치는 경우 과일을 수집하지 않음
            visited.add((x, y))
            result += board[x][y]
    return result

# 입력 받기
N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().strip().split())) for _ in range(N)]
friend_points = []
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    friend_points.append([a - 1, b - 1])

# 각 친구의 가능한 모든 경로 찾기
friends_routes = []
for i in range(M):
    routes = []
    dfs([friend_points[i]], friend_points[i][0], friend_points[i][1], routes)
    friends_routes.append(routes)

# 가능한 모든 경로 조합을 통해 최대 과일 수 찾기
res = 0
for comb in product(*friends_routes):
    res = max(res, get_total_fruits(comb))

print(res)
