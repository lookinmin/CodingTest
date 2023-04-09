# 미로 만들기, G4, 다익스트라
# 되도록 적은 수의 방 바꾸기

from sys import stdin
from collections import deque
import heapq


n = int(stdin.readline().rstrip())
graph = [[] for _ in range(n)]
dist = [[-1] * n for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().rstrip()))

def bfs(x,y):
    q = deque()
    q.append((x,y))
    dist[0][0] = 0


    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if dist[nx][ny] == -1:
                    if graph[nx][ny] == 1:
                        dist[nx][ny] = dist[a][b]
                        q.appendleft((nx,ny))
                    else:
                        dist[nx][ny] = dist[a][b] + 1
                        q.append((nx,ny))

bfs(0,0)
print(dist[n-1][n-1])

#---------------------------------dijkstra------------------------------

def dijkstra():
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    heap = []
    heapq.heappush(heap, [0, 0, 0])     # 거리, x, y
    dist[0][0] = 1
    while heap:
        a, x, y = heapq.heappop(heap)
        if x == n - 1 and y == n - 1:
            print(a)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == 0:
                dist[nx][ny] = 1
                if graph[nx][ny] == 0:
                    heapq.heappush(heap, [a + 1, nx, ny])
                else:
                    heapq.heappush(heap, [a, nx, ny])

dijkstra()