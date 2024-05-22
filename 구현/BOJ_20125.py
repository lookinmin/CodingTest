# 쿠키의 신체 측정, S4
from sys import stdin
n = int(stdin.readline())
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(stdin.readline().rstrip())

dx = [-1, 1, 0, 0]
dy = [0, 0 ,-1, 1]

def chech(a, b):
    cnt = 0
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == '*':
                cnt += 1
    
    if cnt == 4:
        return True

heart = [-1, -1]
for i in range(n):
    for j in range(n):
        if graph[i][j] == '*':
            if chech(i, j):
                heart[0] = i
                heart[1] = j
        

print(heart[0] + 1, heart[1] + 1)

# 왼쪽팔
left_arm = 0
for i in range(heart[1]-1, -1, -1):
    if graph[heart[0]][i] == '*':
        left_arm += 1
    else:
        break
# 오른쪽팔
right_arm = 0
for i in range(heart[1]+1, n):
    if graph[heart[0]][i] == '*':
        right_arm += 1
    else:
        break
# 허리
body = 0
for i in range(heart[0] + 1, n):
    if graph[i][heart[1]] == '*':
        body += 1
    else:
        break
# 왼다리
left_leg = 0
for i in range(heart[0] + body + 1, n):
    if graph[i][heart[1] - 1] == '*':
        left_leg += 1
    else:
        break
# 오른다리
right_leg = 0
for i in range(heart[0] + body + 1, n):
    if graph[i][heart[1] + 1] == '*':
        right_leg += 1
    else:
        break

print(left_arm, right_arm, body, left_leg, right_leg)