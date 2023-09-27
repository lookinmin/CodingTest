# 맥주마시면서 걸어가기, G5, 그래프
# 50m 당 맥주 1
# 출발할 때 맥주 20개
# 박스에는 최대 20개
# node ↔ node가 1000m 이내면 가능

from sys import stdin
from collections import deque

T = int(stdin.readline())

def bfs(a, b):
    q = deque()
    q.append([a,b])

    while q:
        x, y = q.popleft()

        if abs(x - dest[0]) + abs(y-dest[1]) <= 1000:
            print('happy')
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = store[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    q.append([nx, ny])
                    visited[i] = 1
    print('sad')
    return


for _ in range(T):
    n = int(stdin.readline())       # 편의점 개수
    home = list(map(int, stdin.readline().split()))     # 집
    store = []
    for _ in range(n):
        store.append(list(map(int, stdin.readline().split())))
    dest = list(map(int, stdin.readline().split()))
    visited = [0 for _ in range(n+1)]
    bfs(home[0], home[1])
