# 돌 그룹, G4, BFS
from sys import stdin
from collections import deque

A, B, C = map(int, stdin.readline().split())

# 모든 돌의 총 갯수는 고정
# 총 갯수가 3의 배수가 아니라면 돌의 개수가 같아질 수 없음

all = A + B + C
visited = [[0] * (all+1) for _ in range(all+1)]

def bfs():
    global A, B, C, all, visited

    q = deque()
    q.append([A, B])
    visited[A][B] = 1

    while q:
        x, y = q.popleft()

        z = all - x - y

        if x == y == z:
            print(1)
            return

        for a, b in (x, y), (y,z), (x, z):      # 이런식으로 for문을 작성해 두 돌뭉치 간의 돌 갯수를 비교
            if a < b:
                b -= a
                a += a
            elif a > b:
                a -= b
                b += b
            else:       # 돌 수가 같은 두 그룹은 건너뜀
                continue

            c = all - a -b
            x = min(a, b, c)
            y = max(a, b, c)

            if not visited[x][y]:
                q.append([x, y])
                visited[x][y] = 1
    print(0)


if all % 3 != 0:
    print(0)
    exit()
else:
    bfs()
