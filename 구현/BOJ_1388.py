# 바닥 장식, S4, 구현

from sys import stdin

n,m = map(int, stdin.readline().split())

graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(stdin.readline().rstrip())

cnt = 0

for i in range(n):
    a = ''              # 임시로 받아줄 변수 선언
    for j in range(m):
        if graph[i][j] == '-':
            if graph[i][j] != a:
                cnt += 1
        a = graph[i][j]

for j in range(m):
    a = ''
    for i in range(n):
        if graph[i][j] == '|':
            if graph[i][j] != a:
                cnt += 1
        a = graph[i][j]
print(cnt)