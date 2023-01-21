# 행렬, S1, 그리디

from sys import stdin
n, m = map(int,stdin.readline().split())
a = []
b = []
for i in range(n):
    a.append(list(map(int, stdin.readline().strip())))
for i in range(n):
    b.append(list(map(int, stdin.readline().strip())))
cnt = 0

def flip(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            a[x][y] = 1 - a[x][y]


for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            flip(i, j)
            cnt += 1
        if a == b:
            break
    if a == b:
        break

if a != b:
    print(-1)
else:
    print(cnt)