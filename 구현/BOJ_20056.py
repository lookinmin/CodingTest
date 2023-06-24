# 마법사 상어와 파이어볼, G4, 구현

from sys import stdin
from collections import deque

# 파이어볼 입력 = 행, 열, 질량, 이동하는 칸수, 방향

n, m, k = map(int,stdin.readline().split())
graph = [[deque() for _ in range(n)] for _ in range(n) ]        # 그래프의 각 칸을 큐로 만든다
balls = deque()

for _ in range(m):
    r, c, m, s, d = map(int, stdin.readline().split())
    balls.append([r-1,c-1])                     # 파이어볼의 위치를 deque()로
    graph[r-1][c-1].append(deque([m,s,d]))      # 그래프의 각 위치에 해당하는 파이어볼의 값 넣어줌

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):      # k번의 이동
    for j in range(len(balls)):     # 공의 수만큼 이동
        r, c = balls.popleft()
        m, s, d = graph[r][c].popleft()
        nr = (r + s*dx[d]) % n      # 이래야 0 -> n-1로 이동 가능
        nc = (c + s*dy[d]) % n
        graph[nr][nc].append(deque([m,s,d]))        # 이동한 곳으로 파이어볼 옮기기

    for i in range(n):
        for j in range(n):      # 그래프 돌아보면서 탐색
            if len(graph[i][j]) > 1:        # 값이 1초과 -> 파이어볼이 2개이상 해당 위치에 있음
                sum_m, sum_s, odd_d, even_d, cnt = 0,0,0,0,0
                while graph[i][j]:
                    m, s, d = graph[i][j].popleft()
                    sum_m += m
                    sum_s += s
                    cnt += 1
                    if d % 2 == 0:
                        even_d += 1
                    else:
                        odd_d += 1

                sum_m //= 5      # 질량은 합쳐진거 / 5
                if sum_m == 0:
                    continue
                sum_s //= cnt    # 속도는 개수로 나눈다
                if even_d == cnt or odd_d == cnt:       # 모두 홀수이거나 짝수인 경우
                    dir = [0, 2, 4, 6]
                else:
                    dir = [1, 3, 5, 7]
                for d in range(4):
                    balls.append([i, j])
                    graph[i][j].append(deque([sum_m, sum_s, dir[d]]))
            elif len(graph[i][j]) == 1:         # 해당위치에 파이어볼 하나임
                balls.append([i, j])            # 위치 이동
res = 0
for x in range(n):
    for y in range(n):
        for tmp in graph[x][y]:     # 각 위치 m, s, d 리턴
            s = tmp[0]              # m만 가져와서 더함
            res += s

print(res)


