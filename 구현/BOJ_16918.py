# 봄버맨, 실버1, 구현-시물레이션, 그래프 이론
# 처음부터 다시 풀 것

from sys import stdin
from collections import deque

# 1단계
def loc_bomb():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                bomb.append((i, j))


# 3단계
def full_bomb():
    for i in range(r):
        for j in range(c):
            if graph[i][j] != "O":
                graph[i][j] = "O"


# 4단계
def bombs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while bomb:
        a, b = bomb.popleft()
        graph[a][b] = "."

        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            if 0 <= x < r and 0 <= y < c:
                if graph[x][y] == "O":
                    graph[x][y] = "."

r, c, n = map(int, stdin.readline().split())
graph = [list(map(str, stdin.readline().strip())) for _ in range(r)]

n -= 1
while n :
    # 폭탄의 위치를 저장할 리스트
    bomb = deque()

    # 폭탄의 위치 저장
    loc_bomb()

    # 3단계: 모든 칸의 폭탄을 설치
    full_bomb()

    n -= 1
    if n == 0:
        break

    # 4단계: 3초전에 설치된 폭탄 폭발
    bombs()
    n -= 1

for i in graph:
    print("".join(i))

