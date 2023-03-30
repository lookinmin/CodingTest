# 상어 초등학교, G5, 구현

from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())
graph = [[0]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

students = [list(map(int, input().split())) for _ in range(n**2)]
for i in range(n**2):   # 학생 수만큼
    student = students[i]       # 학생 번호
    tmp = []
    for x in range(n):
        for y in range(n):
            if graph[x][y] == 0:
                like = 0
                blank = 0
                for j in range(4):
                    nx = x + dx[j]
                    ny = y + dy[j]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] in student[1:]:        # 4방향 안에 자기가 좋아하는애가 있으면
                            like += 1
                        if graph[nx][ny] == 0:
                            blank += 1                          # 조건2(인접한 칸 중 비어있는 칸이 많은칸 찾기)
                tmp.append([like, blank, x, y])
                # like, blank 값은 클수록, x, y 값은 작을수록 답
    tmp.sort(key = lambda k : (-k[0], -k[1], k[2], k[3]))
    graph[tmp[0][2]][tmp[0][3]] = student[0]            # 제일 우선순위가 높은 자리에 현재 순서의 학생 앉히기

res = 0

students.sort()

for i in range(n):          # 만족도 합 구하기
    for j in range(n):
        ans = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] in students[graph[i][j] - 1]:
                    ans += 1
        if ans:
             res += 10 ** (ans-1)

print(res)
