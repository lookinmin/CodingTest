from sys import stdin
from collections import deque

dx = [-1,0,1,0]  # ^ > v < 
dy = [0,1,0,-1]
direction = ['^', '>', 'v', '<']

h, w = map(int, stdin.readline().split())
graph = [[] for _ in range(h)]
for i in range(h):
    graph[i] = list(map(str, stdin.readline().rstrip()))

# 방문 : #, 미방문 : .

def find_start(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<h and 0<=ny<w and graph[nx][ny] == '#':
            cnt += 1
            tmp = direction[i]
    if cnt > 1:
        return False
    return tmp

visited = [[0] * w for _ in range(h)]

def bfs(a, b):
    q = deque()
    path = deque([])
    q.append([a, b])
    visited[a][b] = 1

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dir = direction[i]

            if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and graph[nx][ny] == '#':
                visited[nx][ny] = 1
                q.append([nx,ny])
                path.append(dir)
    return path

res = ""

for i in range(h):
    for j in range(w):
        if graph[i][j] == '#' and find_start(i, j):
            path = bfs(i, j)
            print(i + 1, j + 1)
            print(path[0])

            cur = path.popleft()
            
            cnt = 1
            for nxt in path:
                if cur == nxt:
                    cnt += 1
                    cur = nxt

                    if cnt % 2 == 0:
                        # 두칸 갔다는거임
                        res+='A'
                        cnt = 0
                else:
                    if direction[direction.index(cur) - 1] == nxt:
                        res += 'L'
                    else:
                        res += 'R'
                    cur = nxt
                    cnt += 1
            print(res)
            exit()