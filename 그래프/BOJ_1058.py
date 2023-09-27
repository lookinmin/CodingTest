# 친구, S2, 그래프

from sys import stdin
from collections import deque
# 2-친구 : A-B가 친구 이거나, A-C-B이거나

n = int(stdin.readline())
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    tmp = list(stdin.readline().rstrip())

    for j in range(len(tmp)):
        if tmp[j] == 'Y':
            graph[i].append(j+1)


def bfs(s):
    dist = [0] * (n + 1)
    dist[s] = 1

    q =deque()
    q.append([s, 0])
    cnt = 0

    while q:
        node, count = q.popleft()

        if count >= 2:
            continue

        for i in range(1, n+1):
            if not dist[i] and (i in graph[node]):
                cnt += 1
                dist[i] = 1
                q.append([i, count + 1])

    return cnt


res = 0
for i in range(1, n+1):
    res = max(res, bfs(i))

print(res)

# ----------- K번 거쳐간다 -> 플로이드 워셜 써야됨

graph2 = [list(stdin.readline().strip()) for _ in range(n)]
f = [[0] * n for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if graph2[i][j] == 'Y' or (graph2[i][k] == 'Y' and graph[k][j] == 'Y'):
                f[i][j] = 1
res = 0

for row in f:
    res = max(res, sum(row))

print(res)