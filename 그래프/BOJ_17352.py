from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

point = 1

if n == 2:
    print("1 2")
    exit(0)

for _ in range(n - 2):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(s):
    global point
    q = deque()
    q.append(s)
    visited[s] = point

    while q:
        now = q.popleft()

        for node in graph[now]:
            if not visited[node]:
                visited[node] = point
                q.append(node)

for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
    point += 1

res = []
for num in visited[1:]:
    if len(res) == 0:
        res.append(num)
    else:
        if num != res[0]:
            res.append(num)
            break

print(*res)